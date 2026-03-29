# 动态生成 tools schema
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.schema_generator import generate_tools_schema

tools_schema = generate_tools_schema()