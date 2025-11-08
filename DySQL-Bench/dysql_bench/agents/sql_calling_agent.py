# Calling SQL code to complete user instruction.

import re
import copy
import json
import requests
from transformers import AutoTokenizer
from typing import List, Optional, Dict, Any

from dysql_bench.agents.base import Agent
from dysql_bench.envs.base import Env
from dysql_bench.types import SolveResult, Action, RESPOND_ACTION_NAME, SQL_ACTION_NAME


class SQLCallingAgent(Agent):
    def __init__(
        self,
        api: str,
        wiki: str,
        model: str,
        temperature: float = 0.6,
        max_tokens: int = 8192,
        top_p: float = 0.95,
        top_k: int = 20,
        min_p: float = 0.0,
    ):
        self.wiki = wiki
        self.model = model
        self.temperature = temperature
        self.api = api
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.top_k = top_k
        self.min_p = min_p

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

            response = requests.post(
                self.api + "/v1/chat/completions", 
                headers={"Content-Type": "application/json"}, 
                json={
                    "messages": messages,
                    "max_tokens": self.max_tokens,
                    "temperature": self.temperature,
                    "top_p": self.top_p,
                    "top_k": self.top_k,
                    "min_p": self.min_p,
                }
            ).json()
            
            next_message = self.parse_response(response['choices'][0]['message']['content'])

            action = message_to_action(next_message)    
            env_response = env.step(action)             
            reward = env_response.reward
            info = {**info, **env_response.info.model_dump()}
            if action.name != RESPOND_ACTION_NAME:
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
        )
    
    def parse_response(self, text):

        think_pattern = r'<think>(.*?)</think>'
        think_match = re.search(think_pattern, text, re.DOTALL)
        reasoning_content = think_match.group(1).strip() if think_match else None

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
        matches = re.findall(sql_pattern, message["content"], re.DOTALL)[0]
        return Action(name=SQL_ACTION_NAME, kwargs={"content": message["content"], "sql": matches})
    else:
        return Action(name=RESPOND_ACTION_NAME, kwargs={"content": message["content"]})