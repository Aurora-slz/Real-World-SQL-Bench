
import os
from openai import OpenAI
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import retry, execute, init_logger
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1,2,3'
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto

# from vllm import LLM,SamplingParams
import json
import jsonlines
import random
import matplotlib.pyplot as plt
from collections import Counter
from tqdm import tqdm
# from vllm import LLM,SamplingParams
import copy
import random
import requests

def load_file(load_path):
    with open(load_path, 'r', encoding='utf-8') as f1:
        data = json.load(f1)
        # print(data[0])
    return data

def save_file(data, save_path):
    with open(save_path, 'w', encoding='utf-8') as f1:
        f1.write(json.dumps(data, ensure_ascii=False, indent=4))


def load_file_2(load_path):
    with open(load_path, 'r', encoding='utf-8') as f1:
        con = []
        for line in f1:
            data = json.loads(line)
            con.append(data)
    #print(con[0])        
    return con




api_url = os.getenv('api_url')
api_key = os.getenv('api_key')
model = os.getenv('verify_model')
MODEL_NAME = model

LOG_NAME = "get_schema"
logger = init_logger(os.getenv('verify_log_path'), LOG_NAME)
logger = logging.getLogger(LOG_NAME)

SYSTEM = """Please help me to verify whether the assistant has solved the user's problem based on the provided user and assistant interactions. 
The user has outlined specific requirements, and the assistant's response should address all of these needs.
The output should indicate whether the assistant has fully addressed the user's request, with a detailed check of the Agent Policy and assistant's sql call validity, correctness of invocation.


You have five principles to do this.
1. [Verification] The output should thoroughly verify whether the assistant's responses and tool calls have correctly addressed all of the user's requests step by step.
2. [SQL Call Accuracy] The output should check whether the assistant used the appropriate sql calls, with correct invocation and parameters, to solve the user's task.
3. [Consistency Check] The output should ensure that the data provided by the user is consistent throughout the interaction, without any discrepancies or hallucinations.
4. [Correctness] The verification should confirm if all of the user's requirements have been fully addressed and that no crucial aspect of the problem was overlooked.


## Response format
The response should include reasoning process step by step, and ending with: "Verification: Is the answer correct (Yes/No)?" followed by "Yes" or "No".
"""

USER_PROMPT = """
Here is the user's requirements:
{user_requirements}

Here is the assistant's response:
{action_outputs}

"""


VOTE_ROUND = int(os.getenv("verify_vote_round"))
print(f"VOTE_ROUND: {VOTE_ROUND}")

with open(os.getenv('verify_wiki'), "r") as f:
    SQL_WIKI = f.read()


@retry(max=5, sleep=1, logger=logger)
def gen_raw_data(line):

    # user_input = USER_PROMPT.format(traj=line['meta']['traj'], user_requirements=line['meta']['info']['task']['instruction'])
    
    line[f'eval_verify_{MODEL_NAME}'] = []

    for i in range(VOTE_ROUND):
        payload = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM.format(domain_rules=SQL_WIKI)},
                {"role": "user", "content": USER_PROMPT.format(user_requirements=line['instruction'], action_outputs=line['actions'])}
            ],
            "temperature": 1.2,
            "top_p": 0.95,
            "max_tokens": 16384
        })

        headers = {
            'Authorization': f"Bearer {api_key}",
            'Content-Type': 'application/json',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }
        # 请求 OpenAI API
        response = requests.post(api_url, headers=headers, data=payload, timeout=1800)
        

        if response.status_code == 200:
            response_data = response.json()
            line[f'eval_verify_{MODEL_NAME}'].append(response_data['choices'][0]['message']['content'])
    return line
        



def cal_score(save_path):
    data = load_file_2(save_path)
    fin_data = []
    
    for i in range(len(data)):
        verify_data = data[i]['eval_verify']

        verify_result = verify_data.rsplit("Verification: Is the answer correct (Yes/No)?", 1)[-1].strip()

        if(verify_result.find("Yes") != -1):
            fin_data.append(data[i])
            
            
    return fin_data


def get_reward1_data(save_path):
    data = load_file(save_path)
    fin_data = []
    for i in range(len(data)):
        if(data[i]['meta']['reward'] == 1):
            fin_data.append(data[i])
    
    return fin_data



input_path = os.getenv('verify_input_path')
verify_save_path = os.getenv('verify_save_path')

print('verify_save_path:', verify_save_path)
# print('split_verify_save_path:', split_verify_save_path)

if __name__ == '__main__':
    data = load_file_2(input_path)
    print(f"before split: {len(data)}")
    
    execute(gen_raw_data, data, verify_save_path, 20, logger, wirte_type='w')
    
    # fin_data = cal_score(verify_save_path)
    # print('after split:', len(fin_data))
    # save_file(fin_data, split_verify_save_path)
