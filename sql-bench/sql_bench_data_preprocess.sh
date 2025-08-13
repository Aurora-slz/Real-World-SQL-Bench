#!/usr/bin/env bash
DATA_PREPROCESS_PY_PATH=/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/sql_bench_data_preprocess.py
RAW_DATA_PATH=/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/music/data/sql/split_verify_tree_EU_music_multiTurn_r1_500_qwen235b_voting11.json
PROCESS_FOLDER_PATH=/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/music/data/process_folder
OUTPUT_FOLDER_PATH=/mnt/public/gpfs-jd/data/lh/guotianyu/sql-bench/tau_bench/envs/music
ENV_NAME=music
VERBOSE=True

python "$DATA_PREPROCESS_PY_PATH" \
    --raw_data_path "$RAW_DATA_PATH" \
    --process_folder_path "$PROCESS_FOLDER_PATH" \
    --output_folder_path "$OUTPUT_FOLDER_PATH" \
    --env_name "$ENV_NAME" \
    --verbose

# 注意修改Mock部分的数据导入, 中间要导入cleaned版本的task