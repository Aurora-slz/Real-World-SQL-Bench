# 操作流程

## Step 1: 安装依赖
```bash
cd sql-bench
```

tau_bench只需要安装sqlparse即可
```bash
pip install sqlparse
```

部署模型需要安装sglang, 可以复用一个之前使用过的sglang环境即可
```bash
pip install sglang[all]
```

## Step 2: 构造数据信息树
这部分可以参考```python build_info_tree_xxxx.py```, 其中```python build_info_tree_v2.py```是使用complex_oracle.sqlite的用户信息树生成代码

## Step 3: 数据预处理在envs文件夹下面，创建文件夹，以任务名称命名（这里以music为例）
### Step 3.1
在envs下创建music文件夹，然后创建data文件夹，在data文件夹下面创建sql文件夹，里面放入slz筛选好的json文件，如```split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11.json```。然后在data文件夹下面写一个__init__.py文件，修改第10行的FILE_NAME为数据库文件名（本例为music.sqlite）。并在data下放入数据库文件（music.sqlite）。

### Step 3.2
在music文件夹下创建__init__.py，env.py，sql-wiki-slz-with-ddl.md和wiki.py。其中sql-wiki-slz-with-ddl.md前面不用动，但是要手动在后面加入数据库的ddl（复制粘贴到sql-wiki-slz-with-ddl.md），用下面这段代码：
```python
import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/retail/data/complex_oracle.sqlite')

# 创建游标对象
cursor = conn.cursor()

# 查询所有表和视图的名称
cursor.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table', 'view');")
items = cursor.fetchall()

# 输出每个表和视图的DDL
for item in items:
    name, obj_type = item
    cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='{obj_type}' AND name='{name}';")
    ddl = cursor.fetchone()[0]
    # print(f"{obj_type.capitalize()} {name} DDL:")
    print(ddl)
    # print("-" * 80)

# 关闭连接
conn.close()
```

### Step 3.3
在env.py中写一个MockMusicEnv类，并在__init__.py中导入这个类
然后需要提前修改这一行代码：
```python
match task_split:               # TODO: 修改成自己的数据
    case "test":
    from tau_bench.envs.music.split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11.executable import TASKS_TEST as tasks

```
注意要先改这个，此时你的目录下并没有这个文件。

## Step 4
先启动一个sglang后端的user模型，因为创建环境是需要user模型的api的，不然不能初始化
```bash
tmux a -t sglang_user_server
export CUDA_VISIBLE_DEVICES=0,1,2,3
python3 -m sglang.launch_server --served-model-name user --model-path /mnt/public/gpfs-jd/data/lh/models/Qwen2.5-72B-Instruct --tp 4 --context-length 32768 --dtype bfloat16 --host 127.0.0.1 --port 30000 --trust-remote-code --disable-overlap --disable-radix-cache > server_user.log 2>&1
```

在tau_bench/envs/__init__.py中加入对应的env_name导入

修改sql_bench_data_preprocess.sh路径，并且运行```bash sql_bench_data_preprocess.sh```
```bash
#!/usr/bin/env bash
# 预处理数据运行文件路径
DATA_PREPROCESS_PY_PATH=/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/sql_bench_data_preprocess.py
# 要处理的文件路径（split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11.json的路径）
RAW_DATA_PATH=/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/music/data/sql/split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11.json
# 这是用来存储中间结果的文件夹，会分别包括一个XXXX_executable.json和XXXX_not_executable.json，表明哪些数据是可执行的，哪些数据不可执行
PROCESS_FOLDER_PATH=/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/music/data/process_folder
# 用来存储输出的过滤后的task文件路径
OUTPUT_FOLDER_PATH=/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/music
# env的名称，就是你在envs中创建的文件夹名称
ENV_NAME=music
VERBOSE=True

python "$DATA_PREPROCESS_PY_PATH" \
    --raw_data_path "$RAW_DATA_PATH" \
    --process_folder_path "$PROCESS_FOLDER_PATH" \
    --output_folder_path "$OUTPUT_FOLDER_PATH" \
    --env_name "$ENV_NAME" \
    --verbose

# 注意修改Mock部分的数据导入, 中间要导入cleaned版本的task
```

## Step 5
在上一步执行完后，修改env.py中的代码。这一步是把刚才筛选的数据选择为我们筛选后的数据(以task开头)
```python
match task_split:               # TODO: 修改成自己的数据
    case "test":
    from tau_bench.envs.music.task_split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11 import TASKS_TEST as tasks
```
下面开始推理，启动agent模型。
```bash
tmux a -t sglang_agent_server
export CUDA_VISIBLE_DEVICES=4,5,6,7
python3 -m sglang.launch_server --served-model-name agent --model-path /mnt/public/gpfs-jd/data/lh/models/Qwen2.5-7B-Instruct --tp 4 --context-length 32768 --dtype bfloat16 --host 127.0.0.1 --port 80 --trust-remote-code --disable-overlap --disable-radix-cache > server_agent.log 2>&1
```

修改sql-bench/run.py中的配置参数。添加对应的env_name
```python
    parser.add_argument(
        "--env", type=str, choices=["retail", "airline", "eu_soccer", "music"], default="retail"
    )
```

修改sql-bench/tau_bench/run.py的配置参数，添加对应的env_name
```python
assert config.env in ["retail", "airline", "eu_soccer", "music"], "Only retail, airline, eu_soccer and music envs are supported"
```

运行多轮对话测评（在sql-bench目录下）
```bash
python run.py --env retail --model /mnt/public/gpfs-jd/data/lh/models/Qwen2.5-7B-Instruct --model-api http://127.0.0.1:80 --max-concurrency 1 --user-model /mnt/public/gpfs-jd/data/lh/models/Qwen2.5-72B-Instruct --user-model-api http://127.0.0.1:30000 --user-strategy llm > run.log 2>&1
```
