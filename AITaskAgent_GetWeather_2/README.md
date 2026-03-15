# AITaskAgent_GetWeather_2

一个简单的天气查询Agent，能够查询指定城市的天气，并将查询结果保存到文件中。
**使用LLM支持的Function Call和Tools Call来进行工具的调用**

**项目结构**

```
AITaskAgent_GetWeather_2
│
├── main.py
├── agent.py
├── llm.py
│
├── tools
│   ├── weather.py
│   ├── registry.py
│   └── file.py
│
└── schemas
    └── tool_schemas.py
```

