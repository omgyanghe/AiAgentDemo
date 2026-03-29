from tools.weather import get_weather
from tools.file import write_file
from tools.decorator import TOOL_REGISTRY

# 自动从装饰器注册表中获取所有工具
TOOLS = {
    name: func for name, func in TOOL_REGISTRY.items()
}

# 手动添加工具（如果没有使用装饰器）
if "get_weather" not in TOOLS:
    TOOLS["get_weather"] = get_weather
if "write_file" not in TOOLS:
    TOOLS["write_file"] = write_file