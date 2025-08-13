

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
Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the sql to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding sql(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions. The new user instruction should have all the parameters for the SQL calls in Actions.

## Guidelines for generating NEW taks instruction and Groundtruth Actions 
1. You must generate a new user instruction according to the <Input Database>.
2. The main focus is to generate actions that can modify the underlying database.  
3. For actions that do not modify the database like specific information requests, scan the provided User Data directly and append only the answer in ‘outputs’. Do not make separate sql calls for this in ‘actions’.  
4. Include multiple SQL calls when the scenario requires multiple steps or modifications.  
5. Provide precise SQL calls with all necessary parameters for each action according to the given Dataset schema, and ALL the parameters should be Explicitly given in the new user instruction.  


## Principles for generating SQL calls
- At the beginning of the conversation, you have to authenticate the user identity by locating their user.
- Once the user has been authenticated, you can provide the user with information, e.g. help the user look up order id.
- You can only help one user per conversation (but you can handle multiple requests from the same user), and must deny any requests for tasks related to any other user.
- You should not make up any information or knowledge or procedures not provided from the user, or give subjective recommendations or comments.
- You should at most make one sql call at a time, and if you take a sql call, you should not respond to the user at the same time. If you respond to the user, you should not make a sql call.
- You should transfer the user to a human agent if and only if the request cannot be handled within the scope of your actions.

## Output Format  
Generate your response according to the following <Instruction Example> and <Format Example> format. Enclose the thought process within ‘<thought></thought>’ tags, and the final structured response within ‘<answer></answer>’ tags. The structured response should be in strict JSON format, without any additional comments or explanations.  


## Instruction Example
{example_instruction}

## Format Example (only for reference)
{{
    "annotator": ...,
    "user_id": "...",
    "instruction": "...",
    "actions": [
        {{
            "sql": "..."
        }},
        {{
            "sql": "..."
        }}
        ...
    ],
    "outputs": []
}}

The new user instruction must have all the parameters for the SQL calls in Actions. Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.
"""

USER_PROMPT = """
## Instructions  
Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the sql to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding sql(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions. ALL SQL parameters in Actions MUST Explicitly given in the new user instruction.

# <Input Database>
The database describes multiple trade records of a certain User. Each trade record includes sales and costs information, as well as details about the involved products.

## User Data  
{sampled_user_details}  

## Trading Data  
{sampled_trade}

## Dataset Schema  
The available Dataset schema in DDL format is as follows:  
{ddl_data}  

Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.  
> The task instruction should involve the relationships between multiple tables, such as considering the connections between a user, sales, costs, and products.
> Remember, Confirm the the generated Instruction have all the parameters in the SQL calls. 
Generate the task now.
"""



save_path = '/m2/slz/sql-bench/output_data/generated_qa/ddl_dbv2_qwen3_235b_1k_0722_multiTurn_v2.json'

def csv_ddl_to_list_pandas(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df.to_dict('records')

ddl_data = csv_ddl_to_list_pandas('/m2/slz/sql-bench/Spider2/spider2-lite/resource/databases/sqlite/complex_oracle/DDL.csv')



with open("/m2/slz/sql-bench/data_pipeline/sql_wiki.md", "r") as f:
    WIKI = f.read()

input_path = '/m2/slz/sql-bench/output_data/db_v2/lean_tree_v2.jsonl'
data = load_file(input_path)



MODEL_NAME = "Qwen3_235B_A22B"
BASE_URL = ".../v1"
API_KEY = "EMPTY"

LOG_NAME = "get_schema"
logger = init_logger("/m2/slz/sql-bench/data_pipeline/log2.log", LOG_NAME)
logger = logging.getLogger(LOG_NAME)

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)






LOG_NAME = "get_schema"
logger = init_logger("/m2/slz/sql-bench/data_pipeline/log.log", LOG_NAME)
logger = logging.getLogger(LOG_NAME)

tasks_path = "/m2/slz/fc/verify/multi_turn_output/extract_qa/r1_tau_r1_5w.json"
tasks = load_file_2(tasks_path)



@retry(max=5, sleep=1, logger=logger)
def gen_raw_data(line):

    random_cust_id = random.randint(0, len(data)-1)
    customer_info = data[random_cust_id]['customer_info']
    customer_info['cust_id'] = data[random_cust_id]['cust_id']

    trade = data[random_cust_id]['trade']
    
    random.shuffle(trade)
    random_trade_number = random.randint(0, len(trade)-1)
    selected_trade = trade[:random_trade_number]

    random_number_task = random.randint(0, len(tasks) - 1)
    example = tasks[random_number_task]['instruction']

    user_input = USER_PROMPT.format(sampled_user_details=customer_info, sampled_trade=selected_trade, ddl_data=ddl_data)
    

    response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM.format(example_instruction=example)},
                {"role": "user", "content": user_input}
            ],
            temperature=1.2,
            top_p=0.95,
            # max_tokens=32768
        )


    line['prompt'] = user_input
    line['generated_data'] = response.choices[0].message.content
    return line
    
        



lines = [{}] * 1000
execute(gen_raw_data, lines, save_path, 20, logger, wirte_type='w')


