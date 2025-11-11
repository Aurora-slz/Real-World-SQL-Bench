# Copyright Sierra

from dysql_bench.envs.base import Env
from dysql_bench.envs.car.data import load_sql_data
from dysql_bench.envs.car.wiki import WIKI
from typing import Optional, Union, List
from dysql_bench.envs.user import UserStrategy

class MockCarEnv(Env):
    def __init__(
        self,
        user_strategy: Union[str, UserStrategy] = UserStrategy.LLM,
        user_model: str = "gpt-4o",
        user_model_api: str = None,
        task_split: str = "test",
        task_index: Optional[int] = None,
        thread_id: int = None
    ):
        match task_split:               # TODO: Modify to your own data
            case "test":
                from dysql_bench.envs.car.tasks_test import TASKS_TEST as tasks
            case _:
                raise ValueError(f"Unknown task split: {task_split}")
        TABLE_NAMES: List[str] = [
            'country', 'price', 'data', 'production'
        ]
        super().__init__(
            data_load_func=load_sql_data,
            table_names=TABLE_NAMES,
            tasks=tasks,
            wiki=WIKI,
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_index=task_index,
            thread_id=thread_id
        )

