# Copyright Sierra

import os
import shutil
import sqlite3

FOLDER_PATH = os.path.dirname(__file__)
FILE_NAME = "complex_oracle.sqlite"
TIMEOUT = 10

def load_sql_data(thread_id: int):
    tmp_folder_path = os.path.join(FOLDER_PATH, "tmp")
    if not os.path.exists(tmp_folder_path):
        os.mkdir(tmp_folder_path)

    # The data storage for the current thread is in the folder tmp/thread_i
    sql_folder_path = os.path.join(tmp_folder_path, f"thread_{thread_id}")
    if not os.path.exists(sql_folder_path):
        os.mkdir(sql_folder_path)
    
    sql_src_path = os.path.join(FOLDER_PATH, FILE_NAME)
    sql_tar_path = os.path.join(sql_folder_path, FILE_NAME)
    shutil.copy(sql_src_path, sql_tar_path)

    conn = sqlite3.connect(sql_tar_path, timeout=TIMEOUT)
    cursor = conn.cursor()
    # The profits table is too large to read in. If the model reads this table incorrectly, it will cause a long time to stall
    cursor.execute(f"DROP VIEW IF EXISTS profits;")                
    return conn, cursor, sql_folder_path
    