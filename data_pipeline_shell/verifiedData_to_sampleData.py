
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
    
    input_path = '/m2/slz/sql-bench/output_data/verified_qa/split_verify_result_Qwen25-72B-Instruct_r1_voting5/verify_result_cleanData_by_qwen25_72b_r1_verify_guazai_step135_voting5.json'
    save_path = "/m2/slz/sql-bench/output_data/example_qa/verified_by_qwen25_72b-r1-toolVerifier.json"
    
    data = load_file(input_path)
    print(len(data))
    final_data = []
    for i in range(0, len(data)):
        final_data.append({"annotator": data[i]['annotator'], 'user_id': data[i]['user_id'], 'instruction': data[i]['instruction'], 'actions': data[i]['actions'], 'outputs': data[i]['outputs']})
    
    save_file(final_data, save_path)
        