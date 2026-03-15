# AITaskAgent_GetWeather_1

一个简单的天气查询Agent，能够查询指定城市的天气，并将查询结果保存到文件中。

**项目结构**

```
AITaskAgent_GetWeather_1
│
├── main.py          # 程序入口
├── agent.py         # Agent核心逻辑
├── llm.py           # LLM调用
├── prompt.py        # Prompt模板
│
├── tools
│   ├── weather.py   # 天气工具
│   ├── file.py      # 文件工具
│   └── registry.py  # 工具注册
│
└── utils
    └── parser.py    # 解析LLM输出
```

**注意：**

使用纯Python的形式调用LLM，而不是使用开源的高级封装库。

另外也没有使用LLM支持的function call或者新版的tools call功能，而是通过**解析LLM输出的文本**，来调用对应的工具。

现在主流的 Agent 已经很少用“解析文本 Action”这种方式了。

现代 Agent 通常使用：

function_call

tool_calls

也就是 结构化工具调用（Structured Tool Calling）。

这样有几个明显优势：
| 方式            | 问题     |
| ------------- | ------ |
| 解析文本 Action   | 容易解析失败 |
| function_call | 稳定     |
| tool_calls    | 支持多工具  |
| JSON schema   | 参数严格   |
