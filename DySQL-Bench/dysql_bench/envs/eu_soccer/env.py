# Copyright Sierra

from tau_bench.envs.base import Env
from tau_bench.envs.eu_soccer.data import load_sql_data
from tau_bench.envs.eu_soccer.wiki import WIKI
from typing import Optional, Union, List
from tau_bench.envs.user import UserStrategy

class MockEUSoccerEnv(Env):
    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_model_api: str = None,
        task_split: str = "test",
        task_index: Optional[int] = None,
        thread_id: int = None
    ):
        match task_split:               # TODO: 修改成自己的数据
            case "test":
                from tau_bench.envs.eu_soccer.tasks_split_verify_tree_EU_soccer_team_multiTurn_r1_500_qwen235b_voting11 import TASKS_TEST as tasks
            case "train":
                from tau_bench.envs.eu_soccer.tasks_train import TASKS_TRAIN as tasks
            case "dev":
                from tau_bench.envs.eu_soccer.tasks_dev import TASKS_DEV as tasks
            case _:
                raise ValueError(f"Unknown task split: {task_split}")
        TABLE_NAMES: List[str] = [
            'sqlite_sequence', 'Player_Attributes', 
            'Player', 'Match', 'League', 'Country', 'Team', 'Team_Attributes'
        ]
        super().__init__(
            data_load_func=load_sql_data,
            table_names=TABLE_NAMES,
            tasks=tasks,                    # 用户发起指令(请求)的数据
            wiki=WIKI,
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_index=task_index,
            thread_id=thread_id
        )

