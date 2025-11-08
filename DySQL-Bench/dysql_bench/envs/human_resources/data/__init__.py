# Copyright Sierra

import json
import os
import shutil
import sqlite3
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)
FILE_NAME = "human_resources.sqlite"
TIMEOUT = 10   # 等待数据库操作时间

def load_data() -> dict[str, Any]:
    with open(os.path.join(FOLDER_PATH, "orders.json")) as f:
        order_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "products.json")) as f:
        product_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "users.json")) as f:
        user_data = json.load(f)
    return {
        "orders": order_data,
        "products": product_data,
        "users": user_data,
    }

def load_sql_data(thread_id: int):
    tmp_folder_path = os.path.join(FOLDER_PATH, "tmp")
    if not os.path.exists(tmp_folder_path):             # Mock环境的路径
        os.mkdir(tmp_folder_path)

    # 当前线程的数据存储在文件夹tmp/thread_i中
    sql_folder_path = os.path.join(tmp_folder_path, f"thread_{thread_id}")
    if not os.path.exists(sql_folder_path):
        os.mkdir(sql_folder_path)
    
    sql_src_path = os.path.join(FOLDER_PATH, FILE_NAME)
    sql_tar_path = os.path.join(sql_folder_path, FILE_NAME)
    shutil.copy(sql_src_path, sql_tar_path)

    conn = sqlite3.connect(sql_tar_path, timeout=TIMEOUT)
    cursor = conn.cursor()              
    return conn, cursor, sql_folder_path
    