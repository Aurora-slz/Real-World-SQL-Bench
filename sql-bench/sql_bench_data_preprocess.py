import argparse
import json
import os
from typing import List
from tqdm import tqdm
from tau_bench.types import Task, Action
from tau_bench.envs import get_env


REQUIRED_KEYS = ["annotator", "user_id", "instruction", "actions", "outputs"]

def validate_and_clean_data(data: List[dict], verbose=False):
    cleaned_data = []
    error_num = 0

    for i, row in enumerate(data):
        try:
            if "outputs" not in row:
                row["outputs"] = []

            assert len(row) == 5, f"Wrong number of keys {len(list(row.keys()))}."       # 缺键
            for key in row:
                assert key in REQUIRED_KEYS

            assert isinstance(row["actions"], list)
            for j, action in enumerate(row["actions"]):
                assert "sql" in action
            assert row["user_id"], "row['user_id'] must not be empty"
            if type(row["user_id"]) == int:
                row['user_id'] = str(row['user_id'])

        except Exception as e:
            if verbose:
                print(f"❌ Error in row {i}: {e}")
            error_num += 1
            continue

        flag = True
        new_outputs = []
        for output in row["outputs"]:
            if isinstance(output, (int, float)):
                new_outputs.append(str(output))
            elif isinstance(output, (list, dict)):
                if verbose:
                    print(f"⚠️ Skipped row {i} due to complex output: {output}")
                flag = False
                break
            elif output is None:
                continue
            else:
                new_outputs.append(output)

        if not flag:
            continue

        row["outputs"] = new_outputs
        cleaned_data.append(row)

    return cleaned_data, error_num


def write_tasks_py(cleaned_data: List[dict], output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("from tau_bench.types import Task, Action\n\n")
        f.write("TASKS_TEST = [\n")
        for row in cleaned_data:
            f.write("   Task(\n")
            f.write(f"      user_id=\"{row['user_id']}\",\n")
            f.write(f"      instruction=\"{row['instruction']}\",\n")
            f.write("       actions=[\n")
            for action in row["actions"]:
                f.write("            Action(\n")
                f.write("               name=\"sql\",\n")
                f.write("               kwargs={\n")
                f.write(f"               \"sql\": \"{action['sql']}\"\n")
                f.write("               }\n")
                f.write("            ),\n")
            f.write("       ],\n")
            f.write(f"       outputs={row['outputs']}\n")
            f.write("   ),\n") 
            
        f.write("]\n")                 # TASKS_TEST=[


def save_cleaned_json(cleaned_data: List[dict], output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        for row in cleaned_data:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def execute_env_tasks(
        cleaned_data_path, 
        cleaned_task_path, 
        process_folder_path,
        output_folder_path, 
        data_name,
        env_name, 
        user_strategy: str = 'llm', 
        user_model: str = "/mnt/public/gpfs-jd/data/lh/models/Qwen2.5-72B-Instruct", 
        user_model_api: str = "http://127.0.0.1:30000",
        task_split: str = "test",
        task_index: int = 0,
        thread_id: int = 0
    ):
    """
    将第一步产生的清理后的数据经过创建环境和执行验证, 得到最后的输出task
    Args:
        cleaned_data_path: 第一步转化为task的清理完的数据, json格式
        cleaned_task_path: 第一步转化为task的清理完的数据, task格式
        process_folder_path: data_executable, data_not_executable的数据文件路径
        output_folder_path:  最终得到的可执行的task的数据文件路径
        data_name: 最终存储的数据名称(task, data_name_executable, data_name_not_executable)
        env_name: 用于选择环境: retail, EU_soccer, music
        user_strategy: 用户是什么交互方法, 默认llm
        user_model: user模型路径
        user_model_api: user模型的api
        task_split: 表明是读入训练集还是测试集
        task_index: 起始位置
        thread_id: 当前编号
    """
    tar_json, error_json = [], []

    with open(cleaned_data_path, "r", encoding="utf-8") as f:
        json_data = [json.loads(line) for line in f]

    executable_ckpt_path = os.path.join(process_folder_path, data_name + '_executable.json')
    if os.path.exists(executable_ckpt_path):
        with open(executable_ckpt_path, 'r', encoding='utf-8') as f:
            for line in f:
                tar_json.append(json.loads(line))

    not_executable_ckpt_path = os.path.join(process_folder_path, data_name + '_not_executable.json')
    if os.path.exists(not_executable_ckpt_path):
        with open(not_executable_ckpt_path, 'r', encoding='utf-8') as f:
            for line in f:
                error_json.append(json.loads(line))

    json_data = json_data[(len(tar_json) + len(error_json)):]
    env = get_env(                      # 一个环境只能执行一个任务, 这里是为了获得tasks
        env_name=env_name,
        user_strategy=user_strategy,
        user_model=user_model,
        user_model_api=user_model_api,
        task_split=task_split,
        task_index=task_index,                   # 这个在验证数据的部分没什么用, 因为我只执行从外面传进来的任务
        thread_id=thread_id
    )
    env.tasks = env.tasks[(len(tar_json) + len(error_json)):]
    # env.tasks = env.tasks[:len(json_data)]
    assert len(env.tasks) == len(json_data), f"len(env.tasks) = {len(env.tasks)}, len(json_data) = {len(json_data)}"

    for idx, task in tqdm(enumerate(env.tasks), total=len(env.tasks)):
        try:
            isolated_env = get_env(                      # 一个环境只能执行一个任务, 这里是为了获得tasks
                env_name=env_name,
                user_strategy=user_strategy,
                user_model=user_model,
                user_model_api=user_model_api,
                task_split=task_split,
                task_index=task_index,
                thread_id=thread_id
            )

            for action in task.actions:
                obs = isolated_env.step(action).observation
                if "Error" in obs:
                    raise ValueError(obs)
            tar_json.append(json_data[idx])

            env.delete_db()

        except Exception as e:
            json_data[idx]["error_info"] = str(e)
            error_json.append(json_data[idx])

    # 保存结果
    with open(executable_ckpt_path, "w", encoding="utf-8") as f:
        for row in tar_json:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    with open(not_executable_ckpt_path, "w", encoding="utf-8") as f:
        for row in error_json:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    task_path = os.path.join(output_folder_path, f"tasks_{data_name}.py")
    write_tasks_py(tar_json, task_path)

    print(f"✅ 可执行任务: {len(tar_json)}, 不可执行任务: {len(error_json)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw_data_path', type=str, required=True)         # 最开始的json路径
    # 过程中其他文件输出路包括data_executable, data_not_executable, raw_data_cleaned的路径
    parser.add_argument('--process_folder_path', type=str, required=True) 
    # output_folder_path:  最终得到的可执行的raw_data_json_cleaned_task, task的数据文件路径
    parser.add_argument('--output_folder_path', type=str, required=True)    
    #parser.add_argument('--data_name', type=str, required=True)             # task的名称
    parser.add_argument('--env_name', type=str, default='complex_oracle')
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()

    raw_data_path = args.raw_data_path
    output_folder_path = args.output_folder_path
    process_folder_path = args.process_folder_path
    env_name = args.env_name

    if not os.path.exists(process_folder_path):
        os.mkdir(process_folder_path)

    data_name = raw_data_path.split('/')[-1].split('.')[0]
    cleaned_data_path = os.path.join(process_folder_path, data_name + '_cleaned.json')
    cleaned_task_path = os.path.join(output_folder_path, data_name + '_cleaned.py')

    # 原始数据
    # 第一阶段: 按照语法进行清洗
    with open(raw_data_path, "r", encoding="utf-8") as f:
        raw_data = [json.loads(line) for line in f]

    cleaned_data, error_num = validate_and_clean_data(raw_data, args.verbose)
    write_tasks_py(cleaned_data, cleaned_task_path)
    save_cleaned_json(cleaned_data, cleaned_data_path)

    print(f"✅ 第一阶段清洗完成，错误数: {error_num}, 有效数: {len(cleaned_data)}")

    execute_env_tasks(
        cleaned_data_path=cleaned_data_path, 
        cleaned_task_path=cleaned_task_path, 
        process_folder_path=process_folder_path,
        output_folder_path=output_folder_path, 
        data_name=data_name,
        env_name=env_name, 

    )
    print(f"✅ 第二阶段清洗完成")

if __name__ == "__main__":
    main()
