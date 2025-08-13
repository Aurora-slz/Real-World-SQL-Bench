# Copyright Sierra

import os
import sqlite3

FOLDER_PATH = os.path.dirname(__file__)

with open(os.path.join(FOLDER_PATH, "sql-wiki-slz-with-ddl.md"), "r") as f:
    WIKI = f.read()
