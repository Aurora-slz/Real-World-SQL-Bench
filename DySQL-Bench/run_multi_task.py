#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
import time
from pathlib import Path

# Available environments (used by interactive menu and argparse choices)
ENV_CHOICES = [
    "pagila", "retail", "bowling", "chinook", "entertainment",
    "eu_soccer", "music", "car", "cookbook", "human_resources",
    "ice_hockey", "law_episode", "retail_world"
]

# Defaults (can be overridden by CLI flags)
DEFAULT_AGENT_MODEL = "Qwen3-4B"
DEFAULT_USER_MODEL  = "Qwen3-4B"
DEFAULT_AGENT_MODEL_API  = "http://127.0.0.1:80"
DEFAULT_USER_MODEL_API   = "http://127.0.0.1:80"
DEFAULT_LOG_DIR          = "logs"
DEFAULT_SLEEP_SEC        = 2
DEFAULT_MAX_CONCURRENCY  = 1
DEFAULT_NUM_TRIALS       = 5

BASE_COMMAND = (
    "python run.py "
    "--env {env} "
    "--model {agent_model_path} "
    "--model-api {agent_model_api} "
    "--max-concurrency {max_concurrency} "
    "--num-trials {num_trials} "
    "--user-model {user_model_path} "
    "--user-model-api {user_model_api} "
    "--user-strategy llm "
    "> {log_dir}/{env}_{model_name}.log 2>&1"
)

def build_command(env, agent_model_path, user_model_path, agent_model_api, user_model_api,
                  log_dir, max_concurrency, num_trials):
    """Build the shell command string for one environment."""
    model_name = Path(agent_model_path).name
    return BASE_COMMAND.format(
        env=env,
        agent_model_path=agent_model_path,
        user_model_path=user_model_path,
        agent_model_api=agent_model_api,
        user_model_api=user_model_api,
        log_dir=log_dir,
        model_name=model_name,
        max_concurrency=max_concurrency,
        num_trials=num_trials
    )

def run_command(env, agent_model_path, user_model_path, agent_model_api, user_model_api,
                log_dir, max_concurrency, num_trials, dry_run=False):
    """Execute a single environment job and wait until it finishes."""
    cmd = build_command(env, agent_model_path, user_model_path, agent_model_api, user_model_api,
                        log_dir, max_concurrency, num_trials)
    print(f"[RUN] {cmd}")
    if dry_run:
        return
    try:
        # Wait for the command to exit; raise CalledProcessError on non-zero return code.
        subprocess.run(cmd, shell=True, check=True)  # per subprocess.run docs
        print(f"[OK ] {env}")
    except subprocess.CalledProcessError as e:
        print(f"[ERR] {env} failed: {e}")

def interactive_select():
    """Simple interactive picker for one/many/all environments."""
    print("Select environments (comma-separated numbers or names), or type 'all' to run all:")
    for idx, name in enumerate(ENV_CHOICES, 1):
        print(f"{idx:2d}) {name}")
    choice = input("> ").strip().lower()
    if choice == "all":
        return ENV_CHOICES[:]

    selected = []
    for token in [x.strip() for x in choice.split(",") if x.strip()]:
        if token.isdigit():
            i = int(token)
            if 1 <= i <= len(ENV_CHOICES):
                selected.append(ENV_CHOICES[i - 1])
            else:
                print(f"Ignored invalid index: {token}")
        else:
            if token in ENV_CHOICES:
                selected.append(token)
            else:
                print(f"Ignored unknown name: {token}")

    # deduplicate while preserving order
    out = []
    for x in selected:
        if x not in out:
            out.append(x)
    if not out:
        print("No valid selection. Exiting.")
        exit(2)
    return out

def parse_args():
    """Parse CLI arguments using argparse (mutually exclusive: --envs vs --all)."""
    p = argparse.ArgumentParser(
        description="Sequentially run SQL benchmark tasks for selected environments "
                    "(supports interactive and CLI modes)."
    )
    g_target = p.add_mutually_exclusive_group()
    g_target.add_argument(
        "-e", "--envs", nargs="+", choices=ENV_CHOICES,
        help="Environment list to run (space-separated)."
    )
    g_target.add_argument(
        "-a", "--all", action="store_true",
        help="Run all environments."
    )
    p.add_argument("--interactive", action="store_true",
                   help="Enter interactive selection (also used by default if neither --envs nor --all is given).")

    p.add_argument("--agent-model", default=DEFAULT_AGENT_MODEL)
    p.add_argument("--user-model",  default=DEFAULT_USER_MODEL)
    p.add_argument("--agent-model-api",  default=DEFAULT_AGENT_MODEL_API)
    p.add_argument("--user-model-api",   default=DEFAULT_USER_MODEL_API)
    p.add_argument("--log-dir",          default=DEFAULT_LOG_DIR)
    p.add_argument("--sleep", type=float, default=DEFAULT_SLEEP_SEC,
                   help="Seconds to sleep between runs.")
    p.add_argument("--max-concurrency", type=int, default=DEFAULT_MAX_CONCURRENCY,
                   help="Value for --max-concurrency passed to run.py.")
    p.add_argument("--num-trials", type=int, default=DEFAULT_NUM_TRIALS,
                   help="Value for --num-trials passed to run.py.")
    p.add_argument("--dry-run", action="store_true",
                   help="Print commands without executing.")
    return p.parse_args()

def main():
    args = parse_args()

    # Ensure log dir exists
    Path(args.log_dir).mkdir(parents=True, exist_ok=True)

    # Decide targets
    if args.all:
        targets = ENV_CHOICES[:]
    elif args.envs:
        targets = args.envs
    else:
        targets = interactive_select()

    for env in targets:
        run_command(
            env=env,
            agent_model_path=args.agent_model,
            user_model_path=args.user_model,
            agent_model_api=args.agent_model_api,
            user_model_api=args.user_model_api,
            log_dir=args.log_dir,
            max_concurrency=args.max_concurrency,
            num_trials=args.num_trials,
            dry_run=args.dry_run
        )
        time.sleep(args.sleep)

if __name__ == "__main__":
    main()
