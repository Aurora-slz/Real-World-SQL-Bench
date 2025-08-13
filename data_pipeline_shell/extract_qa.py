
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
    
    input_path = os.getenv('extract_qa_input_path')
    save_path = os.getenv('extract_qa_save_path')
    
    data = load_file_2(input_path)
    print(len(data))
    extract_data = []
    for i in range(0, len(data)):
        generated_data_i = data[i]['generated_data']
        # 1. 提取 <answer> 和 </answer> 之间的内容
        start_tag = "<answer>"
        end_tag = "</answer>"
        try:
            start_idx = generated_data_i.find(start_tag) + len(start_tag)
            end_idx = generated_data_i.find(end_tag)
            answer_content = generated_data_i[start_idx:end_idx].strip()
            cleaned_content = answer_content.replace('\\n', '').replace('\\"', '"')
            answer_dict = json.loads(cleaned_content)

            extract_data.append(answer_dict)
        except:
            pass
    
    with open(save_path, 'w', encoding='utf-8') as f1:
        for solution in extract_data:        
            f1.write(json.dumps(solution, ensure_ascii=False)+'\n')
        