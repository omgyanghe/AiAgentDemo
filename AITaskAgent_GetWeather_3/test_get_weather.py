#!/usr/bin/env python3
"""
测试 get_weather 工具

使用方法:
    python test_get_weather.py
"""
import json
from tools.weather import get_weather
from tools.decorator import TOOL_REGISTRY


def main():
    print("=" * 60)
    print("测试 get_weather 工具")
    print("=" * 60)
    
    # 1. 测试 Schema
    print("\n【1】Schema 信息:")
    print("-" * 60)
    schema = get_weather._schema
    print(f"函数名：{schema['name']}")
    print(f"描述：{schema['description']}")
    print(f"\n完整 Schema:")
    print(json.dumps(schema, indent=2, ensure_ascii=False))
    
    # 2. 测试类型注解
    print("\n【2】类型注解:")
    print("-" * 60)
    import inspect
    from typing import get_type_hints
    
    sig = inspect.signature(get_weather)
    type_hints = get_type_hints(get_weather)
    print(f"函数签名：{sig}")
    print(f"类型注解：{type_hints}")
    
    # 3. 测试工具注册
    print("\n【3】工具注册:")
    print("-" * 60)
    print(f"已注册的工具：{list(TOOL_REGISTRY.keys())}")
    print(f"get_weather 已注册：{'get_weather' in TOOL_REGISTRY}")
    
    # 4. 测试函数调用
    print("\n【4】函数调用测试:")
    print("-" * 60)
    test_cities = ['Beijing', 'Shanghai', 'Los Angeles']
    for city in test_cities:
        try:
            result = get_weather(city)
            print(f"✓ get_weather('{city}') = {result}")
        except Exception as e:
            print(f"✗ get_weather('{city}') 失败：{e}")
    
    print("\n" + "=" * 60)
    print("测试完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
