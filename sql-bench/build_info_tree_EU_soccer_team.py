# 基于D:\Scientific_Research\sql-bench\build_info_tree_EI_soccer_player_V2.py

import json
import sqlite3
import os
import time
from collections import defaultdict
from tqdm import tqdm

TEAM_LIST = [
    "home_team_api_id",
    "away_team_api_id",
]

PLAYER_LIST = [
    *[f"home_player_{i}" for i in range(1, 12)],
    *[f"away_player_{i}" for i in range(1, 12)],
]

def build_info_tree(base_dir="local_sqlite", output_dir="."):
    start_time = time.time()
    db_path = os.path.join(base_dir, "EU_soccer.sqlite")
    conn = sqlite3.connect(db_path)
    # 性能优化
    conn.execute('PRAGMA synchronous = OFF')
    conn.execute('PRAGMA journal_mode = MEMORY')
    cursor = conn.cursor()

    # 一次性读取所有表
    def fetch_table(name):
        cursor.execute(f"PRAGMA table_info({name})")
        header = {column[1]: column[0] for column in cursor.fetchall()} # 列名: 列号
        cursor.execute(f"SELECT * FROM {name}")
        rows = cursor.fetchall()
        return header, rows

    match_hdr, match_rows = fetch_table("Match")
    player_hdr, player_rows = fetch_table("Player")
    country_hdr, country_rows = fetch_table("Country")
    league_hdr, league_rows = fetch_table("League")
    team_hdr, team_rows = fetch_table("Team")
    attr_hdr, attr_rows = fetch_table("Team_Attributes")

    # 构建映射字典
    player_map = {
        row[player_hdr['player_api_id']]: {
            col: row[idx] for idx, col in enumerate(player_hdr) 
            if col not in ('id')
        }
        for row in player_rows if row[player_hdr['player_api_id']] is not None
    }

    country_map = {
        row[country_hdr['id']]: {
            col: row[idx] for idx, col in enumerate(country_hdr)
        }
        for row in country_rows
    }
    league_map = {
        row[league_hdr['id']]: {
            col: row[idx] for idx, col in enumerate(league_hdr)
        }
        for row in league_rows
    }
    team_map = {
        row[team_hdr['team_api_id']]: {
            col: row[idx] for idx, col in enumerate(team_hdr)
        }
        for row in team_rows
    }

    attrs_map = defaultdict(list)
    for row in attr_rows:
        tid = row[attr_hdr['team_api_id']]
        if tid is None: continue
        info = {col: row[idx] for idx, col in enumerate(attr_hdr) if col not in ('id')}
        attrs_map[tid].append(info)
    
    tree = []
    tid_to_index = {}

    seen_dates = defaultdict(set)

    # 构造树
    for match in tqdm(match_rows,  desc="处理比赛数据", unit="条"):
        match_id = match[match_hdr['match_api_id']]
        # 抽取 match_info，预先填充 country 和 league
        m_info = {col: match[idx] for idx, col in enumerate(match_hdr) if col not in ('id')}
        m_info['country_info'] = country_map.get(match[match_hdr['country_id']], {})
        m_info['league_info'] = league_map.get(match[match_hdr['league_id']], {})

        for team in TEAM_LIST:
            tid = match[match_hdr[team]]
            if tid is None:                 # 当前team不在match里面
                continue
            # 新team节点
            if tid not in tid_to_index:
                tid_to_index[tid] = len(tree)
                tree.append({
                    'player_info': [],
                    'match_info': [],
                    'team_info': dict(team_map.get(tid, {}), team_attributes_info=[])
                })

            # tid_to_index[tid]获得了当前team在tree列表中索引
            node = tree[tid_to_index[tid]]
            # 添加属性信息（按日期去重）
            for attr in attrs_map.get(tid, []):
                date = attr.get('date')
                if date and date not in seen_dates[tid]:
                    seen_dates[tid].add(date)
                    node['team_info']['team_attributes_info'].append(attr)

            # 添加比赛信息
            node['match_info'].append(m_info)

            if "home" in team:
                player_list = PLAYER_LIST[:11]
            else:
                player_list = PLAYER_LIST[11:]
            # 添加player_info
            for player_key in player_list:
                pid = match[match_hdr[player_key]]
                if pid and all(p.get('player_api_id') != pid for p in node['player_info']):
                    p_info = dict(player_map.get(pid, {}))
                    p_info['player_api_id'] = pid
                    node['player_info'].append(p_info)

    # 输出 JSONL
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, 'tree_EU_soccer_team.jsonl')
    with open(out_path, 'w', encoding='utf-8') as fw:
        for record in tqdm(tree,  desc="写入数据", unit="条"):
            fw.write(json.dumps(record, ensure_ascii=False) + "\n")

    with open("example_EU_soccer_team_api_id_8.json", "w", encoding="utf-8") as f:
        json.dump(tree[8], f, indent=4)

    with open("example_EU_soccer_team_api_id_100.json", "w", encoding="utf-8") as f:
        json.dump(tree[100], f, indent=4)

    with open("example_EU_soccer_team_api_id_200.json", "w", encoding="utf-8") as f:
        json.dump(tree[200], f, indent=4)

    print(f"Built tree with {len(tree)} teams in {time.time()-start_time:.2f}s. Saved to {out_path}")

if __name__ == '__main__':
    build_info_tree()