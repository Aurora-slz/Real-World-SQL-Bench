# Copyright Sierra

from tau_bench.envs.base import Env
from tau_bench.envs.pagila.data import load_data, load_sql_data
from tau_bench.envs.pagila.wiki import WIKI
from typing import Optional, Union, List
from tau_bench.envs.user import UserStrategy

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
        match task_split:               # TODO: 修改成自己的数据
            case "test":
                from tau_bench.envs.pagila.tasks_split_verify_refine_split_verify_ddl_gpt41_multiTurn_102_pagila import TASKS_TEST as tasks
            case "train":
                from tau_bench.envs.pagila.tasks_train import TASKS_TRAIN as tasks
            case "dev":
                from tau_bench.envs.pagila.tasks_dev import TASKS_DEV as tasks
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
            tasks=tasks,                    # 用户发起指令(请求)的数据
            wiki=WIKI,
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_index=task_index,
            thread_id=thread_id
        )
        #self.terminate_tools = ["transfer_to_human_agents"]