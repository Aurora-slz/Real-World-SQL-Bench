
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



if __name__ == '__main__':
    
    input_path = os.getenv("INPUT_PATH")
    save_path = os.getenv("SAVE_PATH")
    # input_path = '/m2/slz/sql-bench/output_data/final_bench_data/split_verify_ddl_dbv2_gpt41_0722_multiTurn_500_qwen235b_voting11.json'
    # save_path = "/m2/slz/sql-bench/output_data/final_bench_data/outputs_empty/split_verify_ddl_dbv2_gpt41_0722_multiTurn_500_qwen235b_voting11.json"
    
    data = load_file(input_path)
    print(len(data))
    fin_data = []
    for i in range(0, len(data)):
        if(len(data[i]['outputs']) == 0):
            fin_data.append({'annotator': data[i]['annotator'], 'user_id': data[i]['user_id'], 'instruction': data[i]['instruction'], 'actions': data[i]['actions'], 'outputs': data[i]['outputs']})
    
    with open(save_path, 'w', encoding='utf-8') as f1:
        for solution in fin_data:        
            f1.write(json.dumps(solution, ensure_ascii=False)+'\n')
    print(len(fin_data))
    