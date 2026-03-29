# AITaskAgent_GetWeather_3

一个简单的天气查询Agent，能够查询指定城市的天气，并将查询结果保存到文件中。
**使用LLM支持的Function Call和Tools Call来进行工具的调用**

实现真正的天气查询功能，能够根据用户输入的城市名称查询天气信息。（比如使用天气查询 API 来实现）

**项目结构**

```
AITaskAgent_GetWeather_3
│
├── main.py
│
├── agent
│   ├── agent.py
│   ├── llm.py
│   ├── memory.py
│   └── streaming.py
│
├── tools
│   ├── __init__.py
│   ├── decorator.py
│   ├── registry.py
│   ├── weather.py
│   ├── file.py
│   └── search.py
│
├── schemas
│   └── tool_schema.py
│
└── utils
    └── schema_generator.py
```

