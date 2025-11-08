#####################################################
# 校验数据的键等信息, 并将数据转换为tau_bench的Task格式
#####################################################

import json

data_name = "split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11"
orig_data_path = f"/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/retail/data/sql/{data_name}.json"

json_data = []
with open(orig_data_path, "r", encoding="utf-8") as f:
    for line in f:
        json_data.append(json.loads(line))
print(f"length of {data_name}: {len(json_data)}")
for row in json_data:
    if "outputs" not in row.keys():
        row["outputs"] = []

time = data_name.split("_")[-1]
tar_data_path = f"/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/retail/my_tasks_{data_name}.py"

error_num = 0
keys = ["annotator", "user_id", "instruction", "actions", "outputs"]

tar_jsonl_data = []
with open(tar_data_path, "w", encoding="utf-8") as f:
    f.write("from tau_bench.types import Task, Action\n")
    f.write("\n")
    f.write("TASKS_TEST = [\n")
    for i, row in enumerate(json_data):

        try:
            assert len(list(row.keys())) == 5, f"Wrong number of keys {len(list(row.keys()))}."       # 缺键

            for key in row.keys():
                assert key in keys, f"key {key} is not in ['annotator', 'user_id', 'instruction', 'actions', 'outputs']"
            assert isinstance(row['actions'], list), "type of row['actions'] must be list!"
            for j, action in enumerate(row['actions']):

                assert action.get('sql') is not None, f"each action in row['actions'] must be a dict of 'sql': 'value', {i}row {j}th sql wrong"
            assert row['user_id'], "row['user_id'] must not be empty"

        except Exception as e:
            print(f"Error: row {i} with error: {e}")
            error_num += 1
            continue
        
        flag = True     # 有问题数据flag
        for idx, output in enumerate(row["outputs"]):
            if isinstance(output, int) or isinstance(output, float):
                row["outputs"][idx] = str(output)
            elif isinstance(output, list):
                print(output)
                flag = False
            elif isinstance(output, dict):
                print(output)
                flag = False
            elif output is None:
                row["outputs"].pop(idx)

        if not flag:
            continue

        tar_jsonl_data.append(row)
        
        f.write("   Task(\n")
        f.write(f"      user_id=\"{row['user_id']}\",\n")
        f.write(f"      instruction=\"{row['instruction']}\",\n")
        f.write(f"      actions=[\n")
        for action in row['actions']:
            f.write("            Action(\n")
            f.write("               name=\"sql\",\n")
            f.write("               kwargs={\n")
            f.write(f"               \"sql\": \"{action['sql']}\"\n")
            f.write("               }\n")
            f.write("            ),\n")
        f.write("       ],\n")
        

            
        f.write(f"       outputs={row['outputs']}\n")
        #f.write(f"       outputs=[]\n")
        f.write("   ),\n") 
            
    f.write("]\n")                 # TASKS_TEST=[
    
if "data_executable" not in data_name:
    # 洗过了, 只需要保存tasks就可以
    tar_jsonl_data_path = f"/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/retail/data/sql/{data_name}_cleaned.json"
    with open(tar_jsonl_data_path, "w", encoding="utf-8") as f:
        for row in tar_jsonl_data:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

print(f"error_num: {error_num}")
print("Finished.")

