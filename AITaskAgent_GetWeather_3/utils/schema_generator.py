from tools.decorator import TOOL_REGISTRY

def generate_tools_schema():
    """
    从工具注册表生成 tools schema
    
    :return: tools schema 列表
    """
    tools_schema = []
    
    for name, func in TOOL_REGISTRY.items():
        if hasattr(func, '_schema'):
            schema = func._schema
            tools_schema.append({
                "type": "function",
                "function": {
                    "name": schema["name"],
                    "description": schema["description"],
                    "parameters": schema["parameters"]
                }
            })
    
    return tools_schema

if __name__ == "__main__":
    schema = generate_tools_schema()
    import json
    print(json.dumps(schema, indent=2))