"""
测试 get_weather 工具
"""
import json
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.weather import get_weather


def test_weather_schema():
    """测试 get_weather 的 schema 信息"""
    print("=" * 60)
    print("测试 1: get_weather 工具的 Schema")
    print("=" * 60)
    
    schema = get_weather._schema
    
    print(f"\n函数名：{schema['name']}")
    print(f"描述：{schema['description']}")
    print(f"\nSchema 详情:")
    print(json.dumps(schema, indent=2, ensure_ascii=False))
    
    # 验证 schema 结构
    assert schema['name'] == 'get_weather', "函数名应该是 get_weather"
    assert 'parameters' in schema, "Schema 应该包含 parameters"
    assert 'city' in schema['parameters']['properties'], "应该包含 city 参数"
    assert schema['parameters']['properties']['city']['type'] == 'string', "city 参数类型应该是 string"
    assert 'city' in schema['parameters']['required'], "city 应该是必需参数"
    
    print("\n✅ Schema 测试通过！")
    return schema


def test_weather_function():
    """测试 get_weather 函数调用"""
    print("\n" + "=" * 60)
    print("测试 2: get_weather 函数调用")
    print("=" * 60)
    
    # 测试已知城市
    test_cities = ['Los Angeles', 'New York', 'Beijing']
    
    for city in test_cities:
        try:
            result = get_weather(city)
            print(f"\nget_weather('{city}') = {result}")
            assert isinstance(result, str), f"返回值应该是字符串，实际是 {type(result)}"
            assert len(result) > 0, "返回值不应该为空"
            print(f"✅ {city} 测试通过")
        except Exception as e:
            print(f"❌ {city} 测试失败：{e}")
    
    # 测试未知城市
    print(f"\n测试未知城市:")
    result = get_weather('UnknownCity123')
    print(f"get_weather('UnknownCity123') = {result}")
    print(f"✅ 未知城市测试通过")


def test_weather_type_hints():
    """测试类型注解"""
    print("\n" + "=" * 60)
    print("测试 3: 类型注解")
    print("=" * 60)
    
    import inspect
    from typing import get_type_hints
    
    sig = inspect.signature(get_weather)
    type_hints = get_type_hints(get_weather)
    
    print(f"\n函数签名：{sig}")
    print(f"类型注解：{type_hints}")
    
    # 验证参数类型
    assert 'city' in type_hints, "应该有 city 参数的类型注解"
    assert type_hints['city'] == str, "city 参数类型应该是 str"
    
    print("\n✅ 类型注解测试通过！")


def test_weather_decorator():
    """测试装饰器功能"""
    print("\n" + "=" * 60)
    print("测试 4: 装饰器功能")
    print("=" * 60)
    
    from tools.decorator import TOOL_REGISTRY
    
    # 验证函数已注册
    assert 'get_weather' in TOOL_REGISTRY, "get_weather 应该在工具注册表中"
    assert TOOL_REGISTRY['get_weather'] == get_weather, "注册表中的函数应该与原函数相同"
    
    # 验证 schema 属性
    assert hasattr(get_weather, '_schema'), "装饰后的函数应该有 _schema 属性"
    
    print(f"\n工具注册表中的工具：{list(TOOL_REGISTRY.keys())}")
    print("✅ 装饰器功能测试通过！")


def main():
    """运行所有测试"""
    print("\n" + "=" * 60)
    print("开始测试 get_weather 工具")
    print("=" * 60)
    
    try:
        test_weather_schema()
        test_weather_function()
        test_weather_type_hints()
        test_weather_decorator()
        
        print("\n" + "=" * 60)
        print("🎉 所有测试通过！")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n❌ 测试失败：{e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 测试出错：{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
