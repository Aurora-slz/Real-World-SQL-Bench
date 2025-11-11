# Copyright Sierra

from dysql_bench.envs.base import Env
from dysql_bench.envs.chinook.data import load_sql_data
from dysql_bench.envs.chinook.wiki import WIKI
from typing import Optional, Union, List
from dysql_bench.envs.user import UserStrategy

class MockChinookEnv(Env):
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
                from dysql_bench.envs.chinook.tasks_test import TASKS_TEST as tasks
            case _:
                raise ValueError(f"Unknown task split: {task_split}")
        TABLE_NAMES: List[str] = [
            'albums', 'sqlite_sequence', 'artists', 'customers', 
            'employees', 'genres', 'invoices', 'invoice_items', 
            'media_types', 'playlists', 'playlist_track', 'tracks', 
            'sqlite_stat1'
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

