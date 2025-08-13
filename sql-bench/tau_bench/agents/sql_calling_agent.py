# Calling SQL code to complete user instruction.

import re
import copy
import json
import requests
from transformers import AutoTokenizer
from typing import List, Optional, Dict, Any

from tau_bench.agents.base import Agent
from tau_bench.envs.base import Env
from tau_bench.types import SolveResult, Action, RESPOND_ACTION_NAME, SQL_ACTION_NAME


class SQLCallingAgent(Agent):
    def __init__(
        self,
        api: str,
        wiki: str,
        model: str,
        tokenizer: str = None,
        temperature: float = 0.0,
        
    ):
        self.wiki = wiki
        self.model = model
        self.temperature = temperature
        self.api = api
        if tokenizer is not None:
            self.tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(model)   # 用的和模型相同的tokenizer
    def solve(
        self, env: Env, task_index: Optional[int] = None, max_num_steps: int = 30
    ) -> SolveResult:
        #total_cost = 0.0
        env_reset_res = env.reset(task_index=task_index)
        obs = env_reset_res.observation
        info = env_reset_res.info.model_dump()
        reward = 0.0
        messages: List[Dict[str, Any]] = [
            {"role": "system", "content": self.wiki},
            {"role": "user", "content": obs},
        ]
        for _ in range(max_num_steps):
             # apply chat template
            input_text = self.tokenizer.apply_chat_template(        # 模型是可以看到完整上下文的, 包括报错
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False  
            )

            response = requests.post(
                self.api + "/generate", 
                headers={"Content-Type": "application/json"}, 
                json={
                    "text": input_text,
                    "sampling_params": {
                        "max_new_tokens": 8192,
                        "temperature": 0.6,
                        "top_p": 0.95,
                        "top_k": 20,
                        "min_p": 0.0,
                    }
                }
            ).json()
            
            # extract content from response
            # print("------------------------")
            # print("response.keys(): ", response.keys())
            # if "error" in response:
            #     print("Error in response: ", response['error'])
            # print("------------------------")
            next_message = self.parse_response(response['text'])

            action = message_to_action(next_message)    # 这里的action中的每个sql可能是一个大sql
            env_response = env.step(action)             # 是一个EnvResponse对象
            reward = env_response.reward
            info = {**info, **env_response.info.model_dump()}
            if action.name != RESPOND_ACTION_NAME:
                #print("next_message: ", next_message)
                #next_message["tool_calls"] = next_message["tool_calls"][:1]
                messages.extend(
                    [
                        next_message,
                        {
                            "role": "user",
                            "name": "sql",
                            "content": env_response.observation,
                        },
                    ]
                )
            else:
                messages.extend(
                    [
                        next_message,
                        {"role": "user", "content": env_response.observation},
                    ]
                )
            if env_response.done:
                break
        return SolveResult(
            reward=reward,
            info=info,
            messages=messages,
            #total_cost=total_cost,
        )
    
    def parse_response(self, text):

        think_pattern = r'<think>(.*?)</think>'
        think_match = re.search(think_pattern, text, re.DOTALL)
        reasoning_content = think_match.group(1).strip() if think_match else None

        # 移除所有标签内容(除了)，获取剩余文本
        clean_text = text
        clean_text = re.sub(think_pattern, '', clean_text, flags=re.DOTALL)
        content = clean_text.strip()
    
        return {
            'role': 'agent',
            'raw_response': text,
            'reasoning_content': reasoning_content,
            'content': content
        }

def message_to_action(
    message: Dict[str, Any],
) -> Action:

    if "```sql" in message["content"]:
        sql_pattern = r"```sql(.*?)```"
        matches = re.findall(sql_pattern, message["content"], re.DOTALL)[0]     # 如果有多个sql调用, 只保留第一个
        return Action(name=SQL_ACTION_NAME, kwargs={"content": message["content"], "sql": matches})
    else:
        return Action(name=RESPOND_ACTION_NAME, kwargs={"content": message["content"]})