# Copyright Sierra

from tau_bench.envs.base import Env
from tau_bench.envs.retail.data import load_sql_data
from tau_bench.envs.retail.wiki import WIKI
from typing import Optional, Union, List
from tau_bench.envs.user import UserStrategy

class MockRetailDomainSQLEnv(Env):
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
                from tau_bench.envs.retail.tasks_split_verify_ddl_dbv2_v3_5k_0722_multiTurn_500_qwen235b_voting10 import TASKS_TEST as tasks
            case "train":
                from tau_bench.envs.retail.tasks_train import TASKS_TRAIN as tasks
            case "dev":
                from tau_bench.envs.retail.tasks_dev import TASKS_DEV as tasks
            case _:
                raise ValueError(f"Unknown task split: {task_split}")
        RETAIL_TABLE_NAMES: List[str] = [
        "sales", "costs", "customers", "products", "countries", "times", "promotions", \
        "channels", "supplementary_demographics", "cal_month_sales_mv", "fweek_pscat_sales_mv",\
        "currency"
        ]
        super().__init__(
            data_load_func=load_sql_data,
            table_names=RETAIL_TABLE_NAMES,
            tasks=tasks,                    # 用户发起指令(请求)的数据
            wiki=WIKI,
            # rules=RULES,
            user_strategy=user_strategy,
            user_model=user_model,
            user_model_api=user_model_api,
            task_index=task_index,
            thread_id=thread_id
        )
        #self.terminate_tools = ["transfer_to_human_agents"]