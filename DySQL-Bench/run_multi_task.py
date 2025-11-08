import subprocess
import time

# 读取环境变量列表
# spider2的七个数据库
# envs = ["pagila", "retail", "bowling", "chinook", "entertainment", "eu_soccer", "music"]
# bird的八个数据库
envs = ["car", "cookbook", "disney", "human_resources", "ice_hockey", "law_episode", "retail_word", "social_media"]
# envs = ["retail"]     # 这个还没跑完，应该再跑两个trial
# guotianyu_verl_1机器跑的这个
# agent_model_path = "/mnt/public/gpfs-jd/data/lh/models/OmniSQL-32B"
# cqf_dev_2机器跑的这个
agent_model_path = "/mnt/public/gpfs-jd/data/lh/models/Qwen3-32B"

# 基本命令模板
base_command = (
    "python run.py "
    "--env {env} "
    "--model {model_path} "
    "--model-api http://127.0.0.1:80 "
    # "--model-api http://127.0.0.1:30000 "       # 专用于Qwen2.5-72B-Instruct模型测试
    "--max-concurrency 1 "
    "--num-trials 5 "
    "--user-model /mnt/public/gpfs-jd/data/lh/models/Qwen2.5-72B-Instruct "
    "--user-model-api http://127.0.0.1:30000 "
    "--user-strategy llm "
    "> /mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/results/logs/{env}_{model_name}.log 2>&1"
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
