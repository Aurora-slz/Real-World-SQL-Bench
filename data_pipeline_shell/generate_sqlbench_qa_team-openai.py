
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
Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the sql to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding sql(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions.

## Guidelines for generating NEW taks instruction and Groundtruth Actions 
1. You must generate a new user instruction.
1. The main focus is to generate actions that can modify the underlying database.  
2. For actions that do not modify the database like specific information requests, scan the provided User Data directly and append only the answer in ‘outputs’. Do not make separate tool calls for this in ‘actions’.  
3. Include multiple SQL calls when the scenario requires multiple steps or modifications.  
4. Provide precise SQL calls with all necessary parameters for each action.  
5. Ensure all actions adhere to trade policies and common sense practices.

## Output Format  
Generate your response according to the following format. Enclose the thought process within ‘<thought></thought>’ tags, and the final structured response within ‘<answer></answer>’ tags. The structured response should be in strict JSON format, without any additional comments or explanations.  

## Example format  
{example}  

Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.
"""

USER_PROMPT = """
## Instructions  
Generate a NEW task instruction that mimics realistic human users and their intentions, such as with different personality and goals. The task instruction should be followed by ‘actions’ which is a list of the sql to be taken to solve this task and ‘outputs’ which is a list of the answers to specific information requests made by the user. Think step by step to come up with the action(s) and the corresponding sql(s) translating this thought that would be necessary to fulfill the user’s request or solve their intentions.

## Guidelines for Generating Task Instruction
{domain_rules}  

## Player Data  
{sampled_user_details}  

## Match Data  
{sampled_trade}


## Tools  
The available database schema in DDL format is as follows:  
{ddl_data}  

Do not directly copy instruction and the action patterns from the examples. Ground the generation from the above provided data.  
Generate the task now.
"""



save_path = '/m2/slz/sql-bench/team_output_data/generated_qa/tree_EU_soccer_team.json'

def csv_ddl_to_list_pandas(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df.to_dict('records')

ddl_data = csv_ddl_to_list_pandas('/m2/slz/sql-bench/Spider2/spider2-lite/resource/databases/sqlite/EU_soccer/DDL.csv')



with open("/m2/slz/sql-bench/data_pipeline/sql_wiki.md", "r") as f:
    WIKI = f.read()

input_path = '/m2/slz/sql-bench/team_output_data/tree_EU_soccer_team.jsonl'
data = load_file_2(input_path)





tasks_path = "/m2/slz/sql-bench/output_data/example_qa/verified_by_qwen25_72b-r1-toolVerifier.json"
tasks = load_file(tasks_path)


@retry(max=5, sleep=1, logger=logger)
def gen_raw_data(line):

    random_cust_id = random.randint(0, len(data)-1)
    
    player_info = data[random_cust_id]['player_info']
    # sample_player_number = random.randint(0, 15)
    random.shuffle(player_info)
    # player_info = player_info[:sample_player_number]
    

    match_info = data[random_cust_id]['match_info']
    random.shuffle(match_info)
    random_trade_number = random.randint(0, 15)
    match_info = match_info[:random_trade_number]

    random_number_task = random.randint(0, len(tasks) - 1)
    example = tasks[random_number_task]
    # example = {
    #     "annotator": 0,
    #     "user_id": "mortimer_valentino_3167",
    #     "instruction": "You are Mortimer Valentino, a cautious individual who recently moved to 22 Palm Grove Boulevard. You wish to update your street address in the system and provide a new home phone number: 713-555-0198. Ensure changes are processed securely and confirm your birth year remains correct.",
    #     "actions": [
    #         {
    #             "sql": "SELECT * FROM customers WHERE cust_first_name = 'Mortimer' AND cust_last_name = 'Valentino' AND cust_email = 'Valentino@company.example.com' AND cust_main_phone_number = '668-223-3167';"
    #         },
    #         {
    #             "sql": "UPDATE customers SET cust_street_address = '22 Palm Grove Boulevard', cust_main_phone_number = '713-555-0198' WHERE cust_email = 'Valentino@company.example.com' AND cust_main_phone_number = '668-223-3167';"
    #         },
    #     ],
    #     "outputs": [],
    # }

    # user_input = USER_PROMPT.format(domain_rules=WIKI, sampled_user_details=customer_info, sampled_trade=selected_trade)
    user_input = USER_PROMPT.format(domain_rules=WIKI, sampled_user_details=player_info, sampled_trade=match_info, ddl_data=ddl_data)


    response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM.format(example=example)},
                {"role": "user", "content": user_input}
            ],
            temperature=1.2,
            top_p=0.95,
            # max_tokens=32768
        )

    
    line['prompt'] = user_input
    line['generated_data'] = response.choices[0].message.content
    return line
    
        



lines = [{}] * 10000
execute(gen_raw_data, lines, save_path, 20, logger, wirte_type='w')


