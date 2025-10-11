# Operation Process

## Step 1: Install Dependencies
```bash
cd sql-bench
```

 only requires installing sqlparse
```bash
pip install sqlparse
```

Deploying the model requires installing sglang. You can reuse a previously used sglang environment.
```bash
pip install sglang[all]
```

## Step 2: Construct Data Information Tree
This part can refer to ```python build_info_tree_xxxx.py```, where ```python build_info_tree_v2.py``` is the code for generating the information tree using the complex_oracle.sqlite user data.

## Step 3: Data Preprocessing. Under the envs folder, create a folder named after the task (using 'music' as an example here).
### Step 3.1
Create a 'music' folder under envs, then create a 'data' folder. Under the 'data' folder, create an 'sql' folder and place the JSON files filtered by slz inside, such as ```split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11.json```. Then, write an __init__.py file under the 'data' folder, modifying the FILE_NAME on line 10 to the database file name (in this case, music.sqlite). Also, place the database file (music.sqlite) under 'data'.

### Step 3.2
Create __init__.py, env.py, sql-wiki-slz-with-ddl.md, and wiki.py under the 'music' folder. The front part of sql-wiki-slz-with-ddl.md doesn't need changes, but you need to manually append the DDL of the database to sql-wiki-slz-with-ddl.md (copy and paste it), using the following code snippet:
```python
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('/sql-bench/envs/retail/data/complex_oracle.sqlite')

# Create a cursor object
cursor = conn.cursor()

# Query the names of all tables and views
cursor.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table', 'view');")
items = cursor.fetchall()

# Output the DDL for each table and view
for item in items:
    name, obj_type = item
    cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='{obj_type}' AND name='{name}';")
    ddl = cursor.fetchone()[0]
    # print(f"{obj_type.capitalize()} {name} DDL:")
    print(ddl)
    # print("-" * 80)

# Close the connection
conn.close()
```

### Step 3.3
Write a MockMusicEnv class in env.py, and import this class in __init__.py.
Then, you need to modify this line of code in advance:
```python
match task_split:               # TODO: Change to your own data
    case "test":
    from envs.music.split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11.executable import TASKS_TEST as tasks

```
Note: You need to change this first, even though the corresponding file does not exist in your directory at this moment.

## Step 4
First, start a sglang backend user model because creating the environment requires the user model's API; otherwise, initialization will fail.
```bash
tmux a -t sglang_user_server
export CUDA_VISIBLE_DEVICES=0,1,2,3
python3 -m sglang.launch_server --served-model-name user --model-path /models/Qwen2.5-72B-Instruct --tp 4 --context-length 32768 --dtype bfloat16 --host 127.0.0.1 --port 30000 --trust-remote-code --disable-overlap --disable-radix-cache > server_user.log 2>&1
```

Add the corresponding env_name import in envs/__init__.py.

Modify the path in sql_bench_data_preprocess.sh and run ```bash sql_bench_data_preprocess.sh```
```bash
#!/usr/bin/env bash
# Preprocessing data script path
DATA_PREPROCESS_PY_PATH=/sql-bench/sql_bench_data_preprocess.py
# Path to the file to be processed (path to split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11.json)
RAW_DATA_PATH=/sql-bench/envs/music/data/sql/split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11.json
# This folder is used to store intermediate results, which will include XXXX_executable.json and XXXX_not_executable.json, indicating which data is executable and which is not.
PROCESS_FOLDER_PATH=/sql-bench/envs/music/data/process_folder
# Path to store the output filtered task files
OUTPUT_FOLDER_PATH=/sql-bench/envs/music
# The env name, which is the folder name you created under envs
ENV_NAME=music
VERBOSE=True

python "$DATA_PREPROCESS_PY_PATH" \
    --raw_data_path "$RAW_DATA_PATH" \
    --process_folder_path "$PROCESS_FOLDER_PATH" \
    --output_folder_path "$OUTPUT_FOLDER_PATH" \
    --env_name "$ENV_NAME" \
    --verbose

# Note: Modify the data import for the Mock part, need to import the cleaned version of the task in the middle.
```

## Step 5
After the previous step finishes executing, modify the code in env.py. This step selects the data we filtered in the previous step as our data (starting with 'task').
```python
match task_split:               # TODO: Change to your own data
    case "test":
```
Now start the inference and launch the agent model.
```bash
tmux a -t sglang_agent_server
export CUDA_VISIBLE_DEVICES=4,5,6,7
python3 -m sglang.launch_server --served-model-name agent --model-path /models/Qwen2.5-7B-Instruct --tp 4 --context-length 32768 --dtype bfloat16 --host 127.0.0.1 --port 80 --trust-remote-code --disable-overlap --disable-radix-cache > server_agent.log 2>&1
```

Run the multi-turn dialogue evaluation (under the sql-bench directory)
```bash
python run.py --env retail --model /models/Qwen2.5-7B-Instruct --model-api http://127.0.0.1:80 --max-concurrency 1 --user-model /models/Qwen2.5-72B-Instruct --user-model-api http://127.0.0.1:30000 --user-strategy llm > run.log 2>&1
```
