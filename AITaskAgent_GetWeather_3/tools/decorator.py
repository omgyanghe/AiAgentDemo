import inspect
from typing import get_type_hints, get_origin, get_args

TOOL_REGISTRY = {}

def _python_type_to_json_type(python_type):
    """
    将 Python 类型转换为 JSON Schema 类型
    
    :param python_type: Python 类型
    :return: JSON Schema 类型字符串
    """
    if python_type is None:
        return "string"
    
    origin = get_origin(python_type)
    
    if origin is None:
        type_mapping = {
            str: "string",
            int: "integer",
            float: "number",
            bool: "boolean",
            list: "array",
            dict: "object",
        }
        return type_mapping.get(python_type, "string")
    
    if origin is list or origin is tuple:
        return "array"
    elif origin is dict:
        return "object"
    elif origin is type:
        # 处理 type[X] 的情况，提取 X 的类型
        args = get_args(python_type)
        if args:
            return _python_type_to_json_type(args[0])  # ✅ 递归处理内部类型
        return "string"

    return "string"

def tool(func):
    """
    工具装饰器，用于注册工具函数并生成 schema
    
    :param func: 要装饰的函数
    :return: 装饰后的函数
    """
    TOOL_REGISTRY[func.__name__] = func
    
    # 获取函数签名信息
    sig = inspect.signature(func)
    doc = func.__doc__ or ""
    
    # 获取类型注解
    try:
        type_hints = get_type_hints(func)
    except Exception:
        type_hints = {}
    
    # 存储函数的 schema 信息
    func._schema = {
        "name": func.__name__,
        "description": doc.strip().split('\n')[0] if doc else "",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
    
    # 解析参数
    for param_name, param in sig.parameters.items():
        param_type = type_hints.get(param_name, str)
        json_type = _python_type_to_json_type(param_type)
        
        param_schema = {
            "type": json_type,
            "description": f"{param_name} parameter"
        }
        
        func._schema["parameters"]["properties"][param_name] = param_schema
        
        if param.default == inspect.Parameter.empty:
            func._schema["parameters"]["required"].append(param_name)
    
    return func