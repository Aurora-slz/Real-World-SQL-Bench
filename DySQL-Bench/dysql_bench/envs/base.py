# Copyright Sierra

import os
import time
import shutil
import random
import sqlite3
import sqlparse
from hashlib import sha256
from tau_bench.envs.tool import Tool
from typing import Any, Callable, Dict, List, Type, Optional, Set, Union, Tuple

from tau_bench.envs.user import load_user, UserStrategy
from tau_bench.types import (
    Action,
    Task,
    EnvInfo,
    EnvResetResponse,
    EnvResponse,
    RewardResult,
    RewardOutputInfo,
    RewardActionInfo,
    RESPOND_ACTION_NAME,
    SQL_ACTION_NAME
)

import re

VOLATILE_COL_RE = re.compile(
    r"(?i)^(last_?update|updated_?at|update_?time|modified(_at)?|modification_?time|create(d)?_?at|timestamp)$"
)
IGNORE_TABLES = {"sqlite_sequence", "sqlite_stat1"}


ToHashable = Union[
    # 一行数据是一个元组
    str, int, float, Dict[str, "ToHashable"], List["ToHashable"], Set["ToHashable"], tuple["ToHashable"]
]
Hashable = Union[str, int, float, Tuple["Hashable"], Tuple[Tuple[str, "Hashable"]]]


def to_hashable(item: ToHashable) -> Hashable:
    if isinstance(item, dict):
        return tuple((key, to_hashable(value)) for key, value in sorted(item.items()))
    elif isinstance(item, list):
        return tuple(to_hashable(element) for element in item)
    elif isinstance(item, set):
        return tuple(sorted(to_hashable(element) for element in item))
    else:
        return item


def consistent_hash(
    value: Hashable,
) -> str:
    return sha256(str(value).encode("utf-8")).hexdigest()


# 改成不支持工具调用的模式了, 不支持tool了
class Env(object):
    def __init__(
        self,
        data_load_func: Callable[[], Dict[str, Any]],
        table_names: List[str],
        tasks: List[Task],
        wiki: str,
        # rules: List[str],
        user_strategy: Union[str, UserStrategy],
        user_model: str,
        user_model_api: str,
        task_index: Optional[int] = None,
        thread_id: Optional[int] = None
    ) -> None:
        super().__init__()
        self.data_load_func = data_load_func
        self.conn, self.cursor, self.sql_folder_path = data_load_func(thread_id)     # 返回一个数据库cursor
        self.thread_id = thread_id
        self.user_model_api = user_model_api

        self.tasks = tasks
        if task_index is not None:
            self.task_index = task_index
        else:
            self.task_index = random.randint(0, len(tasks) - 1) # 左闭右闭区间
        self.task = tasks[self.task_index]
        self.table_names = table_names

        self.wiki = wiki
        # self.rules = rules
        self.user = load_user(              # 暂时先不改, 回头看一下(应该不用改)
            api=self.user_model_api, user_strategy=user_strategy, model=user_model
        )
        self.actions: List[Action] = []

    def reset(self, task_index: Optional[int] = None) -> EnvResetResponse:
        if task_index is None:
            task_index = random.randint(0, len(self.tasks))
        self.task_index = task_index

        self.conn, self.cursor, self.sql_folder_path = self.data_load_func(self.thread_id)   # 会重新复制, 然后重新返回一个新的cursor
        self.task = self.tasks[task_index]
        self.actions = []
        initial_observation = self.user.reset(instruction=self.task.instruction)
        return EnvResetResponse(
            observation=initial_observation, info=EnvInfo(task=self.task, source="user")
        )

    def step(self, action: Action) -> EnvResponse:
        self.actions.append(action)

        info = EnvInfo(task=self.task)
        reward = 0
        done = False
        
        if action.name == RESPOND_ACTION_NAME: 
            # action.kwargs: {"name": "xxx", "content": "xxx"}
            observation = self.user.step(action.kwargs["content"])
            info.source = "user"
            done = "###STOP###" in observation
        elif action.name == SQL_ACTION_NAME:
            sql_start_time = time.time()  # 记录SQL执行开始时间
            observation = ""
            try:
                # action.kwargs: {"name": "xxx", "content": "xxx", "sql": "xxx"}
                sql_code = action.kwargs["sql"]
                sql_list = sqlparse.split(sql_code)  # 分割成多个sql原子语句
                for sql in sql_list:                 # 每个sql是一个基本操作(SELECT, INSERT, UPDATE, DELETE等)
                    sql = sql.strip()                # 去掉前后空格
                    # 获取sql语句类型(SELECT, INSERT, UPDATE, DELETE等)
                    sql_type = sqlparse.parse(sql)[0].get_type().upper()  
                    self.cursor.execute(sql)          # 注意这里返回的是cursor
                    if sql_type == "SELECT":
                        rows = self.cursor.fetchall()
                        observation += f"<result>{rows}</result>\n"
                    else:
                        observation += f"<result>SQL execution Successfully!</result>\n"
                        self.conn.commit()  # 提交事务, 确保数据被写入数据库, 否则数据库会被锁定
                sql_end_time = time.time()  # 记录SQL执行结束时间
                print(f"执行成功时间: {sql_end_time - sql_start_time:.2f}s")

            except Exception as e:
                observation += f"<result>Error: {e}\n</result>"
                print(observation)
                self.conn.rollback()  # 回滚事务, 确保数据库状态不变
                sql_end_time = time.time()  # 记录SQL执行结束时间
                print(f"执行回滚时间: {sql_end_time - sql_start_time:.2f}s")

            info.source = action.name   
            # if action.name in self.terminate_tools:   # 不知道有什么操作会触发这个问题, 所以暂时不管了
            #     done = True

        else:
            observation = f"Unknown action {action.name}"
            info.source = action.name

        if done:
            calculate_reward_start_time = time.time()
            reward_res = self.calculate_reward()
            reward = reward_res.reward
            info.reward_info = reward_res
            #info.user_cost = self.user.get_total_cost()
            # 需要删除掉数据库, 避免占用过多空间
            self.delete_db()
            calculate_reward_end_time = time.time()
            print(f"计算奖励时间: {calculate_reward_end_time - calculate_reward_start_time:.2f}s")
            
        return EnvResponse(observation=observation, reward=reward, done=done, info=info)

    def get_data_hash(self) -> str:
        """
        读出所有表的所有数据, 计算哈希值.
        这里必须是读出所有数据, 否则可能目标表格最后模型修改正确了, 但是在搜索过程中错误修改了其他表格
        """
        all_data = []                       
        # 获取所有真实表
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        all_tables = {row[0] for row in self.cursor.fetchall()} - {"sqlite_sequence", "sqlite_stat1"}

        for table in self.table_names:
            if table not in all_tables:
                continue

            self.cursor.execute(f'PRAGMA table_info("{table}")')
            cols_info = self.cursor.fetchall()
            cols = [c[1] for c in cols_info]

            if not cols:
                all_data.append((table, ()))
                continue

            # 忽略易变列
            stable_cols = [c for c in cols if not VOLATILE_COL_RE.match(c)]

            if stable_cols:
                sel = ", ".join(f'"{c}"' for c in stable_cols)
                ob = ", ".join(f'"{c}"' for c in stable_cols)
                # 最后加 rowid 保证稳定顺序
                self.cursor.execute(f'SELECT {sel} FROM "{table}" ORDER BY {ob}, rowid')
                rows = self.cursor.fetchall()
                all_data.append((table, tuple(rows)))
            else:
                self.cursor.execute(f'SELECT COUNT(*) FROM "{table}"')
                n = self.cursor.fetchone()[0]
                all_data.append((table, ("__ONLY_ROWCOUNT__", n)))

        return consistent_hash(to_hashable(all_data))

    def calculate_reward(self) -> RewardResult:
        data_hash = self.get_data_hash()            # agent处理完之后, 计算结束状态数据库哈希值
        self.conn.close()  # 关闭连接, 后面重新复制数据库, 重新打开连接

        reward = 1.0
        actions = [                                 # 获得所有的sql语句
            action for action in self.task.actions if action.name != RESPOND_ACTION_NAME
        ]

        # Check if the database changes are correct. If they are not correct, then we set the reward to 0.
        # TODO: cache gt_data_hash in tasks.py (low priority)
        self.conn, self.cursor, reward_sql_folder_path = self.data_load_func(self.thread_id)   # 重新复制数据库, 返回conn, cursor      
        
        assert self.sql_folder_path == reward_sql_folder_path, "Different sqlite database when calculating reward!"

        # 如果task中包含ground truth的sql语句, 就用这个, 否则需要重新写 
        for action in self.task.actions:
            #if action.name not in self.terminate_tools:
            #    self.step(action)
            self.step(action)                       # 执行所有的sql

        gt_data_hash = self.get_data_hash()

        # 计算奖励完毕
        self.conn.close()
        
        info = RewardActionInfo(
            r_actions=data_hash == gt_data_hash, gt_data_hash=gt_data_hash
        )
        if not info.r_actions:
            reward = 0.0
        else:
            print("hash_check:", data_hash, " and ", gt_data_hash)

        if len(self.task.outputs) > 0:
            # check outputs
            r_outputs = 1.0
            outputs = {}
            for output in self.task.outputs:
                found = False
                for action in self.actions:         # 遍历agent生成的每个sql语句
                    if (
                        action.name == RESPOND_ACTION_NAME
                        and output.lower()
                        in action.kwargs["content"].lower().replace(",", "")
                    ):
                        found = True
                        break
                outputs[output] = found
                if not found:
                    r_outputs = 0.0
                    reward = 0.0
            info = RewardOutputInfo(r_outputs=r_outputs, outputs=outputs)
            
        return RewardResult(reward=reward, info=info, actions=actions)

    def delete_db(self):
        shutil.rmtree(self.sql_folder_path)