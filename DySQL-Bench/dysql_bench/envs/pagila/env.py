# Copyright Sierra

from dysql_bench.envs.base import Env
from dysql_bench.envs.pagila.data import load_sql_data
from dysql_bench.envs.pagila.wiki import WIKI
from typing import Optional, Union, List
from dysql_bench.envs.user import UserStrategy

class MockPagilaEnv(Env):
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
                from dysql_bench.envs.pagila.tasks_test import TASKS_TEST as tasks
            case _:
                raise ValueError(f"Unknown task split: {task_split}")
        TABLE_NAMES: List[str] = [
            'actor', 'country', 'city', 
            'address', 'language', 'category', 
            'customer', 'film', 'film_actor', 
            'film_category', 'film_text', 'inventory', 
            'staff', 'store', 'payment', 'rental', 
            'customer_list', 'film_list', 'staff_list', 
            'sales_by_store', 'sales_by_film_category'
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