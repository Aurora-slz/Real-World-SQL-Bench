# Copyright Sierra

import os
import json
import time
import random
import threading
import traceback
from math import comb
from tqdm import tqdm
from typing import List
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from dysql_bench.envs import get_env
from dysql_bench.agents.base import Agent
from dysql_bench.types import EnvRunResult, RunConfig
from dysql_bench.envs.user import UserStrategy

MAX_NUM_STEPS = 30

def run(config: RunConfig) -> List[EnvRunResult]:
    assert config.env in ["retail", "eu_soccer", "music", "bowling", "entertainment", "pagila", "chinook", "car", "cookbook", "human_resources", "ice_hockey", "law_episode", "retail_world"], f"Only retail, eu_soccer, music, bowling, entertainment, pagila, chinook, car, cookbook, human_resources, ice_hockey, law_episode, retail_world envs are supported"
    assert config.agent_strategy in ["sql"], "Invalid agent strategy"  # TODO: add other agent strategies in the future
    assert config.task_split in ["test"], "Invalid task split"   # TODO: add other task splits in the future
    assert config.user_strategy in [item.value for item in UserStrategy], "Invalid user strategy"

    random.seed(config.seed)
    time_str = datetime.now().strftime("%m%d%H%M%S")
    ckpt_path = f"{config.log_dir}/results/{config.env}-{config.agent_strategy}-agent-{config.model.split('/')[-1]}-{config.temperature}_range_{config.start_index}-{config.end_index}_user-{config.user_model.split('/')[-1]}-{config.user_strategy}_{time_str}.json"
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)

    print(f"Loading user with strategy: {config.user_strategy}")
    env = get_env(              
        config.env,             
        user_strategy=config.user_strategy,
        user_model=config.user_model,
        user_model_api=config.user_model_api,
        task_split=config.task_split,
        thread_id=None
    )
    agent = agent_factory(
        api=config.model_api,
        wiki=env.wiki,
        config=config,
    )
    end_index = (
        len(env.tasks) if config.end_index == -1 else min(config.end_index, len(env.tasks))
    )
    results: List[EnvRunResult] = []
    lock = threading.Lock()  
    if config.task_ids and len(config.task_ids) > 0:
        print(f"Running tasks {config.task_ids} (checkpoint path: {ckpt_path})")
    else:
        print(
            f"Running tasks {config.start_index} to {end_index} (checkpoint path: {ckpt_path})"
    )
    for i in range(config.num_trials):
        if config.task_ids and len(config.task_ids) > 0:
            idxs = config.task_ids
        else:
            idxs = list(range(config.start_index, end_index))
        if config.shuffle:
            random.shuffle(idxs)

        def _run(idx: int) -> EnvRunResult:
            run_start_time = time.time()
            print(f"idx:{idx}, _run start time: {run_start_time:.2f}")
            thread_id = threading.get_ident()  
            print(f"Thread ID: {thread_id} processing index {idx}")
            isolated_env = get_env(
                env_name=config.env,
                user_strategy=config.user_strategy,
                user_model=config.user_model,
                user_model_api=config.user_model_api,
                task_split=config.task_split,
                task_index=idx,
                thread_id=thread_id
            )

            print(f"Running task {idx}")
            try:
                res = agent.solve(
                    env=isolated_env,
                    task_index=idx,
                    max_num_steps=MAX_NUM_STEPS
                )
                result = EnvRunResult(
                    task_id=idx,
                    reward=res.reward,
                    info=res.info,
                    traj=res.messages,
                    trial=i,
                )
            except Exception as e:
                result = EnvRunResult(
                    task_id=idx,
                    reward=0.0,
                    info={"error": str(e), "traceback": traceback.format_exc()},
                    traj=[],
                    trial=i,
                )
            print(
                "✅" if result.reward == 1 else "❌",
                f"task_id={idx}",
                result.info,
            )
            print("-----")
            run_end_time = time.time()
            print(f"idx:{idx}, _run agent.solve finish needs time: {(run_end_time - run_start_time): .2f}")
            with lock:
                lock_start_time = time.time()
                print(f"idx:{idx}, lock wait time: {(lock_start_time - run_end_time): .2f}")
                data = []
                if os.path.exists(ckpt_path):
                    with open(ckpt_path, "r") as f:
                        data = json.load(f)
                with open(ckpt_path, "w") as f:
                    json.dump(data + [result.model_dump()], f, indent=2)
                print(f"idx:{idx}, lock write time: {(time.time() - lock_start_time): .2f}")
            return result

        with ThreadPoolExecutor(max_workers=config.max_concurrency) as executor:
            res = list(tqdm(executor.map(_run, idxs), total=len(idxs), desc=f"Trial {i+1}/{config.num_trials}"))
            results.extend(res)

    display_metrics(results)

    with open(ckpt_path, "w") as f:
        json.dump([result.model_dump() for result in results], f, indent=2)
        print(f"\n📄 Results saved to {ckpt_path}\n")
    return results


def agent_factory(
    api: str, 
    wiki, config: RunConfig
) -> Agent:
    if config.agent_strategy == "sql":
        from dysql_bench.agents.sql_calling_agent import SQLCallingAgent

        return SQLCallingAgent(
            api=api,
            wiki=wiki,
            model=config.model,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            top_p=config.top_p,
            top_k=config.top_k,
            min_p=config.min_p,
        )

    else:
        raise ValueError(f"Unknown agent strategy: {config.agent_strategy}")


def display_metrics(results: List[EnvRunResult]) -> None:
    def is_successful(reward: float) -> bool:
        return (1 - 1e-6) <= reward <= (1 + 1e-6)

    num_trials = len(set([r.trial for r in results]))
    rewards = [r.reward for r in results]
    avg_reward = sum(rewards) / len(rewards)
    # c from https://arxiv.org/pdf/2406.12045
    c_per_task_id: dict[int, int] = {}
    for result in results:
        if result.task_id not in c_per_task_id:
            c_per_task_id[result.task_id] = 1 if is_successful(result.reward) else 0
        else:
            c_per_task_id[result.task_id] += 1 if is_successful(result.reward) else 0
    pass_hat_ks: dict[int, float] = {}
    for k in range(1, num_trials + 1):
        sum_task_pass_hat_k = 0
        for c in c_per_task_id.values():
            sum_task_pass_hat_k += comb(c, k) / comb(num_trials, k)
        pass_hat_ks[k] = sum_task_pass_hat_k / len(c_per_task_id)
    print(f"🏆 Average reward: {avg_reward}")
    print("📈 Pass^k")
    for k, pass_hat_k in pass_hat_ks.items():
        print(f"  k={k}: {pass_hat_k}")
