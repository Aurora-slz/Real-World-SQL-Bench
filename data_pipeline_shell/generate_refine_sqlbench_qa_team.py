
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
from vllm import LLM,SamplingParams
import copy
import random
import requests
import pandas as pd





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

import random







# SYSTEM = """
# Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the tool_calls to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding tool_call(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions. Focus on common retail scenarios following the provided task instruction guidelines.

# ## Guidelines for generating NEW taks instruction and Groundtruth Actions 
# 1. You must generate a new user instruction.
# 1. The main focus is to generate actions that can modify the underlying database.  
# 2. For actions that do not modify the database like specific information requests, scan the provided User Data directly and append only the answer in ‘outputs’. Do not make separate tool calls for this in ‘actions’.  
# 3. Include multiple tool calls when the scenario requires multiple steps or modifications.  
# 4. Provide precise tool calls with all necessary parameters for each action.  
# 5. Ensure all actions adhere to retail policies and common sense practices.

# ## Output Format  
# Generate your response according to the following format. Enclose the thought process within ‘<thought></thought>’ tags, and the final structured response within ‘<answer></answer>’ tags. The structured response should be in strict JSON format, without any additional comments or explanations.  

# ## Example format  
# {example}  

# Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.
# """

# USER_PROMPT = """
# ## Instructions  
# Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the tool_calls to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding tool_call(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions. Focus on common retail scenarios following the provided task instruction guidelines.  

# ## Guidelines for Generating Task Instruction
# {domain_rules}  

# ## User Data  
# {sampled_user_details}  

# ## Trading Data  
# {sampled_trade}


# Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.  
# Generate the task now.
# """

SYSTEM = """
REFINE the given task to confirm the the refined instruction have all the parameters in the SQL calls. Think step-by-step to improve the instruction and corresponding SQL queries. 

## Guidelines for Refining Task Instruction and Groundtruth Actions  
1. Start with an existing task instruction and enhance its realism or clarity.  
2. Focus on ensuring actions can properly modify the underlying database.  
3. For non-modifying actions (e.g., information requests), scan the provided User Data directly and append only the answer in 'outputs'—no separate tool calls needed in 'actions'.  
4. Adjust SQL calls if the refined scenario requires additional or modified steps.  
5. Ensure SQL calls include all necessary parameters based on the Dataset schema, and ALL parameters must be explicitly given in the refined instruction.  
6. Refined SQL parameters MUST align with the updated user instruction.  

## Output Format  
Provide your response in the following format. Enclose the thought process within ‘<thought></thought>’ tags, and the final structured response within ‘<answer></answer>’ tags. The structured response should be in strict JSON format, without additional comments.  


The refined instruction must include all parameters for the SQL calls in Actions.
"""

USER_PROMPT = """
## Guidelines for Refining Task Instruction
{domain_rules}  

## Given Task
{given_taks}  


## Dataset Schema  
The available Dataset schema in DDL format is as follows:  
{ddl_data}  

Refine the task now.
"""



save_path = '/m2/slz/sql-bench/team_output_data/generated_qa/tree_EU_soccer_team_r1_500_refine.json'

def csv_ddl_to_list_pandas(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df.to_dict('records')

ddl_data = csv_ddl_to_list_pandas('/m2/slz/sql-bench/Spider2/spider2-lite/resource/databases/sqlite/EU_soccer/DDL.csv')



with open("/m2/slz/sql-bench/data_pipeline/sql_wiki.md", "r") as f:
    WIKI = f.read()




api_url = "http://123.129.219.111:3000/v1/chat/completions"
api_key = ""
model='deepseek-r1'

LOG_NAME = "get_schema"
logger = init_logger("/m2/slz/sql-bench/data_pipeline/log.log", LOG_NAME)
logger = logging.getLogger(LOG_NAME)

lines = []
tasks_path = "/m2/slz/sql-bench/team_output_data/verified_qa/tree_EU_soccer_team_r1_500/split_verify_split_verify_tree_EU_soccer_team_r1_500_qwen235b_voting20_r1_voting5.json"
tasks = load_file(tasks_path)
for i in range(len(tasks)):
    tasks[i] = {'instruction': tasks[i]['instruction'], 'actions': tasks[i]['actions'], 'outputs': tasks[i]['outputs']}
    tasks[i]['user_id'] = 'user_' + str(i)
    tasks[i]['annotator'] = 0
    lines.append({'original_task': tasks[i]})

@retry(max=5, sleep=1, logger=logger)
def gen_raw_data(line):

    example = line['original_task']


    user_input = USER_PROMPT.format(domain_rules=WIKI, given_taks=example, ddl_data=ddl_data)

    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM.format(example=example)},
            {"role": "user", "content": user_input}
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
        line['prompt'] = user_input
        line['generated_data'] = response_data['choices'][0]['message']['content']
        return line
    
        



execute(gen_raw_data, lines, save_path, 20, logger, wirte_type='w')


