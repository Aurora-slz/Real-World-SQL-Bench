
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



def cal_score(save_path):
    data = load_file_2(save_path)
    print('base: ', len(data))
    fin_data = []
    
    for i in range(len(data)):

        # verify_data_list = data[i]['eval_verify']
        # verify_data_list = data[i]['eval_verify_qwen3_235b'] 
        verify_data_list = data[i]['eval_verify_deepseek-r1'] 
        yes_count = 0
        no_count = 0

        for verify_data in verify_data_list:
            verify_result = verify_data.split("Verification: Is the answer correct (Yes/No)?")[-1].strip()
            if(verify_result.find("Yes") != -1):
                yes_count += 1                
            elif(verify_result.find("No") != -1):
                no_count += 1
        print(f"yes_count: {yes_count}, no_count: {no_count}")
        if(yes_count >= no_count):
            fin_data.append(data[i])
        # if(yes_count == 0):
        #     fin_data.append(data[i])
            
    return fin_data


def get_reward1_data(save_path):
    data = load_file(save_path)
    fin_data = []
    for i in range(len(data)):
        if(data[i]['meta']['reward'] == 1):
            fin_data.append(data[i])
    
    return fin_data



# input_path = "/data_train/code/sft_intern/slz/sql-bench/output_data/verified_qa/data_executable_ddl_r1_5k_0627/verify_result_Qwen25-72B-Instruct_voting5.json"
# split_verify_save_path = "/data_train/code/sft_intern/slz/sql-bench/output_data/verified_qa/data_executable_ddl_r1_5k_0627/split_verify_result_Qwen25-72B-Instruct_voting5.json"

input_path = os.getenv('verify_split_input_path')
split_verify_save_path = os.getenv('verify_split_save_path')
if __name__ == '__main__':
    
    fin_data = cal_score(input_path)
    print('after split:', len(fin_data))
    # save_file(fin_data, split_verify_save_path)

    with open(split_verify_save_path, 'w', encoding='utf-8') as f1:
        for solution in fin_data:        
            f1.write(json.dumps(solution, ensure_ascii=False)+'\n')


