
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
# Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the sql to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding sql(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions.

# ## Guidelines for generating NEW taks instruction and Groundtruth Actions 
# 1. You must generate a new user instruction.
# 1. The main focus is to generate actions that can modify the underlying database.  
# 2. For actions that do not modify the database like specific information requests, scan the provided User Data directly and append only the answer in ‘outputs’. Do not make separate tool calls for this in ‘actions’.  
# 3. Include multiple SQL calls when the scenario requires multiple steps or modifications.  
# 4. Provide precise SQL calls with all necessary parameters for each action.  
# 5. Ensure all actions adhere to trade policies and common sense practices.

# ## Output Format  
# Generate your response according to the following format. Enclose the thought process within ‘<thought></thought>’ tags, and the final structured response within ‘<answer></answer>’ tags. The structured response should be in strict JSON format, without any additional comments or explanations.  

# ## Example format  
# {example}  

# Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.
# """

# USER_PROMPT = """
# ## Instructions  
# Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the sql to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding sql(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions.

# ## Guidelines for Generating Task Instruction
# {domain_rules}  

# ## User Data  
# {sampled_user_details}  

# ## Trading Data  
# {sampled_trade}


# ## Tools  
# The available database schema in DDL format is as follows:  
# {ddl_data}  

# Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.  
# Generate the task now.
# """

SYSTEM = """
Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the sql to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding sql(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions. The new user instruction should have all the parameters for the SQL calls in Actions.

## Guidelines for generating NEW taks instruction and Groundtruth Actions 
1. You must generate a new user instruction.
2. The main focus is to generate actions that can modify the underlying database.  
3. For actions that do not modify the database like specific information requests, scan the provided User Data directly and append only the answer in ‘outputs’. Do not make separate tool calls for this in ‘actions’.  
4. Include multiple SQL calls when the scenario requires multiple steps or modifications.  
5. Provide precise SQL calls with all necessary parameters for each action according to the given Dataset schema, and ALL the parameters should be Explicitly given in the new user instruction.  
6. Generated SQL parameters MUST align with the new user instruction.


## Output Format  
Generate your response according to the following format. Enclose the thought process within ‘<thought></thought>’ tags, and the final structured response within ‘<answer></answer>’ tags. The structured response should be in strict JSON format, without any additional comments or explanations.  

## Example format (only for reference)
{example}  

The new user instruction must have all the parameters for the SQL calls in Actions. Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.
"""

USER_PROMPT = """
## Instructions  
Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the sql to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding sql(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions. ALL SQL parameters in Actions MUST Explicitly given in the new user instruction.

## Guidelines for Generating Task Instruction
{domain_rules}  

## Player Data  
{sampled_user_details}  

## Match Data  
{sampled_trade}


## Dataset Schema  
The available Dataset schema in DDL format is as follows:  
{ddl_data}  

Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.  
> Remember, Confirm the the generated Instruction have all the parameters in the SQL calls. 
Generate the task now.
"""





save_path = '/m2/slz/sql-bench/team_output_data/generated_qa/tree_EU_soccer_team_r1_500.json'

def csv_ddl_to_list_pandas(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df.to_dict('records')

ddl_data = csv_ddl_to_list_pandas('/m2/slz/sql-bench/Spider2/spider2-lite/resource/databases/sqlite/EU_soccer/DDL.csv')


with open("/m2/slz/sql-bench/data_pipeline/sql_wiki.md", "r") as f:
    WIKI = f.read()

input_path = '/m2/slz/sql-bench/team_output_data/tree_EU_soccer_team.jsonl'
data = load_file_2(input_path)




api_url = "http://123.129.219.111:3000/v1/chat/completions"
api_key = ""
model='deepseek-r1'

LOG_NAME = "get_schema"
logger = init_logger("/m2/slz/sql-bench/data_pipeline/log.log", LOG_NAME)
logger = logging.getLogger(LOG_NAME)

tasks_path = "/m2/slz/sql-bench/output_data/verified_qa/ddl_dbv2_r1_5k_0719_refine/split_verify_dbv2_r1_5k_0719_500_qwen235b_voting10.json"
tasks = load_file(tasks_path)
for i in range(len(tasks)):
    tasks[i] = {'instruction': tasks[i]['instruction'], 'actions': tasks[i]['actions'], 'outputs': tasks[i]['outputs']}
    tasks[i]['user_id'] = 'user_' + str(i)
    tasks[i]['annotator'] = 0

@retry(max=5, sleep=1, logger=logger)
def gen_raw_data(line):

    random_cust_id = random.randint(0, len(data)-1)
    
    player_info = data[random_cust_id]['player_info']
    # sample_player_number = random.randint(0, 15)
    random.shuffle(player_info)
    # player_info = player_info[:sample_player_number]
    

    match_info = data[random_cust_id]['match_info']
    random.shuffle(match_info)
    random_trade_number = random.randint(5, 15)
    match_info = match_info[:random_trade_number]

    random_number_task = random.randint(0, len(tasks) - 1)
    example = tasks[random_number_task]

    # user_input = USER_PROMPT.format(domain_rules=WIKI, sampled_user_details=customer_info, sampled_trade=selected_trade)
    user_input = USER_PROMPT.format(domain_rules=WIKI, sampled_user_details=player_info, sampled_trade=match_info, ddl_data=ddl_data)

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
    
        



lines = [{}] * 500
execute(gen_raw_data, lines, save_path, 20, logger, wirte_type='w')


