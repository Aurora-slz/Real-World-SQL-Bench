#!/bin/bash
set -e  # 脚本遇到错误时立即退出
set -u  # 使用未定义变量时报错




export input_path="/m2/slz/sql-bench/output_data/db_v2/lean_tree_v2.jsonl"
export save_path="/m2/slz/sql-bench/test_output_data/generated_qa/ddl_dbv2_gpt41_0722_multiTurn_500.json"
export generate_num=10
export ddl_data="/m2/slz/sql-bench/Spider2/spider2-lite/resource/databases/sqlite/complex_oracle/DDL.csv"
export example_data="/m2/slz/fc/verify/multi_turn_output/extract_qa/r1_tau_r1_5w.json"
export api_url="http://123.129.219.111:3000/v1/chat/completions"
export api_key=""
export model="gpt-4.1"
export log_path="/m2/slz/sql-bench/data_pipeline_shell/log.log"
python /m2/slz/sql-bench/data_pipeline_shell/generate_sqlbench_multiTurn_qa.py


export extract_qa_input_path="$save_path"
export extract_qa_save_path="/m2/slz/sql-bench/test_output_data/extract_qa/$(basename "$extract_qa_input_path")"
python /m2/slz/sql-bench/data_pipeline_shell/extract_qa.py







export verify_input_path="$extract_qa_save_path"
echo "verify_input_path: $verify_input_path"
export verify_save_path="/m2/slz/sql-bench/test_output_data/verified_qa/verify_$(basename "$verify_input_path").json"
export verify_vote_round=1
export verify_model="deepseek-r1"
export verify_log_path="/m2/slz/sql-bench/data_pipeline_shell/log_verify.log"
export verify_wiki="/m2/slz/sql-bench/data_pipeline/verify_sql_wiki.md"
python /m2/slz/sql-bench/data_pipeline_shell/verify_qa_voting_request.py


export verify_split_input_path="$verify_save_path"
export verify_split_save_path="/m2/slz/sql-bench/test_output_data/verified_qa/split_$(basename "$verify_split_input_path").json"
python /m2/slz/sql-bench/data_pipeline_shell/verify_qa_voting_then_split.py









export refine_input_data="$verify_split_save_path"
export refine_save_path="/m2/slz/sql-bench/test_output_data/generated_qa/refine_$(basename "$refine_input_data").json"
export refine_wiki="/m2/slz/sql-bench/data_pipeline/sql_wiki.md"
export refine_model="deepseek-r1"
export refine_log_path="/m2/slz/sql-bench/data_pipeline_shell/log_refine.log"
python /m2/slz/sql-bench/data_pipeline_shell/generate_refine_sqlbench_qa.py


export extract_qa_input_path="$refine_save_path"
export extract_qa_save_path="/m2/slz/sql-bench/test_output_data/extract_qa/$(basename "$extract_qa_input_path")"
python /m2/slz/sql-bench/data_pipeline_shell/extract_qa.py











export verify_input_path="$extract_qa_save_path"
export verify_save_path="/m2/slz/sql-bench/test_output_data/generated_qa/verify_$(basename "$verify_input_path").json"
export verify_vote_round=5
export verify_model="deepseek-r1"
export verify_log_path="/m2/slz/sql-bench/data_pipeline_shell/log_verify.log"
export verify_wiki="/m2/slz/sql-bench/data_pipeline/verify_sql_wiki.md"
python /m2/slz/sql-bench/data_pipeline_shell/verify_qa_voting_request.py


export verify_split_input_path="$verify_save_path"
export verify_split_save_path="/m2/slz/sql-bench/test_output_data/verified_qa/split_$(basename "$verify_split_input_path").json"
python /m2/slz/sql-bench/data_pipeline_shell/verify_qa_voting_then_split.py



echo "$extract_qa_save_path"
