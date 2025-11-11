# Copyright Sierra

import argparse
from dysql_bench.types import RunConfig
from dysql_bench.run import run
from dysql_bench.envs.user import UserStrategy


def parse_args() -> RunConfig:
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-trials", type=int, default=1)
    parser.add_argument(
        "--env", type=str, choices=["retail", "airline", "eu_soccer", "music", "bowling", "entertainment", "pagila", "chinook", "car", "cookbook", "disney", "human_resources", "ice_hockey", "law_episode", "retail_world", "social_media"], default="retail"
    )
    parser.add_argument(
        "--model",
        type=str,
        help="The model to use for the agent",
    )
    parser.add_argument(
        "--model-api",
        type=str,
        default="http://127.0.0.1:80",
        help="The model to use for the agent",
    )    
    parser.add_argument(
        "--user-model",
        type=str,
        default="gpt-4o",
        help="The model to use for the user simulator",
    )
    parser.add_argument(
        "--user-model-api",
        type=str,
        default="http://127.0.0.1:80",
        help="The model's api to use for the user simulator",
    )
    parser.add_argument(
        "--agent-strategy",
        type=str,
        default="sql",
        choices=["sql"],
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.6,
        help="The sampling temperature for the action model",
    )
    parser.add_argument(
    "--max_tokens",
    type=int,
    default=8192,
    help="The maximum number of tokens to generate for each model output",
    )
    parser.add_argument(
        "--top_k",
        type=int,
        default=20,
        help="The top_k hyperparameter for the action model (number of tokens to sample from)",
    )

    parser.add_argument(
        "--top_p",
        type=float,
        default=0.95,
        help="The top_p (nucleus sampling) parameter for the action model; lower = more focused sampling",
    )

    parser.add_argument(
        "--min_p",
        type=float,
        default=0.0,
        help="The minimum probability threshold for token sampling (used in min_p sampling)",
    )
    parser.add_argument(
        "--task-split",
        type=str,
        default="test",
        choices=["test"],
        help="The split of tasks to run",
    )
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--end-index", type=int, default=-1, help="Run all tasks if -1")
    parser.add_argument("--task-ids", type=int, nargs="+", help="(Optional) run only the tasks with the given IDs")
    parser.add_argument("--log-dir", type=str, default="results")
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=1,
        help="Number of tasks to run in parallel",
    )
    parser.add_argument("--seed", type=int, default=10)
    parser.add_argument("--shuffle", type=int, default=0)
    parser.add_argument("--user-strategy", type=str, default="llm", choices=[item.value for item in UserStrategy])

    args = parser.parse_args()
    print(args)
    return RunConfig(
        model=args.model,
        model_api=args.model_api,
        user_model=args.user_model,
        user_model_api=args.user_model_api,
        num_trials=args.num_trials,
        env=args.env,
        agent_strategy=args.agent_strategy,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        top_k=args.top_k,
        top_p=args.top_p,
        min_p=args.min_p,
        task_split=args.task_split,
        start_index=args.start_index,
        end_index=args.end_index,
        task_ids=args.task_ids,
        log_dir=args.log_dir,
        max_concurrency=args.max_concurrency,
        seed=args.seed,
        shuffle=args.shuffle,
        user_strategy=args.user_strategy,
    )


def main():
    config = parse_args()
    run(config)


if __name__ == "__main__":
    main()
