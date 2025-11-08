TODO: 
- user和agent模型调用接口改成本地的   ——   使用sglang本地部署模型包装成API, 无需修改接口(测试完成, 部署的是不使用工具调用版本)
- sql_calling_agent.py构造调用sql语句的agent  —— 暂时完成(需要测试样例检查是否正确)
- Env基类修改(如果要兼容工具调用和sql语句的话, 则需要添加新的调用符号(必需, 保持相同逻辑), 类似RESPOND_ACTION_NAME)
- 奖励计算, 需要读入整个数据库然后计算奖励(tau-bench的数据库是json文件)