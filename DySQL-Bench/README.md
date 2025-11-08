# 创建环境
```bash
conda create -n venv python=3.10
cd ./real_world_sql_bench_with_15_databases
conda activate venv
pip install sqlparse
pip install "sglang[all]"  # 也可以单开一个环境装sglang
```

# 部署模型，这里以我自己本地部署为例
部署user模型
默认的user模型是Qwen2.5-72B-Instruct, api是http://127.0.0.1:30000
```bash
tmux a -t sglang_user_server
export CUDA_VISIBLE_DEVICES=0,1,2,3
python3 -m sglang.launch_server --served-model-name user --model-path /mnt/public/gpfs-jd/data/lh/models/Qwen2.5-72B-Instruct --tp 4 --context-length 32768 --dtype bfloat16 --host 127.0.0.1 --port 30000 --trust-remote-code --disable-overlap --disable-radix-cache > server_user.log 2>&1
```

部署agent模型
默认api是http://127.0.0.1:80
```bash
tmux a -t sglang_agent_server
export CUDA_VISIBLE_DEVICES=4,5,6,7
python3 -m sglang.launch_server --served-model-name agent --model-path /mnt/public/gpfs-jd/data/lh/models/Qwen3-32B --tp 4 --context-length 32768 --dtype bfloat16 --host 127.0.0.1 --port 80 --trust-remote-code --disable-overlap --disable-radix-cache > server_agent.log 2>&1
```

# 可能需要配置一下agents部分
tau_bench\agents\sql_calling_agent.py下我向agent里传入了agent的模型路径，因为需要用到tokenizer。
你看一下如果调用远程api的话是怎么调用的(可能不需要tokenizer)，可以对这个部分进行修改

# 启动命令
在当前目录下创建一个文件夹results用于存放结果, 并且在其中分别创建两个文件夹logs(存放日志)和results(存放结果)
```bash
python run_multi_task.py
```

run_multi_task.pyz注释
```python
import subprocess
import time

# envs是环境名称
# spider2的七个数据库
# envs = ["pagila", "retail", "bowling", "chinook", "entertainment", "eu_soccer", "music"]
# bird的八个数据库
envs = ["car", "cookbook", "disney", "human_resources", "ice_hockey", "law_episode", "retail_word", "social_media"]
agent_model_path = "/mnt/public/gpfs-jd/data/lh/models/Qwen3-32B"

# 基本命令模板
# 注意每一行字符串最后有个空格
base_command = (
    "python run.py "            # 启动命令
    "--env {env} "                # 环境名称    
    "--model {model_path} "      # 模型路径(或名称，用于传入tau_bench\agents\sql_calling_agent.py和results中结果和日志的文件命名)
    "--model-api http://127.0.0.1:80 "  # agent模型的api
    # "--model-api http://127.0.0.1:30000 "       # 专用于Qwen2.5-72B-Instruct模型测试
    "--max-concurrency 1 "      # 并发数量
    "--num-trials 5 "           # 测试次数
    "--user-model /mnt/public/gpfs-jd/data/lh/models/Qwen2.5-72B-Instruct "  # user模型的路径(或名称)
    "--user-model-api http://127.0.0.1:30000 "  # user模型的api
    "--user-strategy llm "      # user模型的策略
    "> /mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/results/logs/{env}_{model_name}.log 2>&1" # 日志路径
)

# 执行命令的函数
def run_command(env, model_path):
    model_name = agent_model_path.split('/')[-1]
    command = base_command.format(env=env, model_path=model_path, model_name=model_name)
    print(f"Executing command: {command}")
    try:
        # 使用 subprocess.run() 确保每个命令执行完成后再继续
        subprocess.run(command, shell=True, check=True)
        print(f"Command for {env} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command for {env}: {e}")

# 主循环，按顺序执行每个环境
for env in envs:
    run_command(env, agent_model_path)
    # 如果需要，可以加一个时间间隔
    time.sleep(2)  # 可以调整等待时间，避免过于频繁的执行
```
