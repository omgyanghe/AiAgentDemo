from llm import call_llm
from prompt import SYSTEM_PROMPT
from tools.registry import TOOLS
from utils.parser import parse_action
import json
import inspect

class Agent:

    def run(self, user_input):

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]

        while True:

            response = call_llm(messages)

            print("\nLLM:", response)

            if "Final Answer" in response:
                return response

            action, action_input = parse_action(response)

            if action in TOOLS:

                func = TOOLS[action]
                # 获取函数签名
                sig = inspect.signature(func)
                # 获取参数信息
                params = list(sig.parameters.keys())
                
                # 解析 action_input 为 JSON
                # !!! 这里要注意参数量为多个的情况。
                try:
                    input_data = json.loads(action_input)
                    # 如果是字典，按参数名传递
                    if isinstance(input_data, dict):
                        result = func(**input_data)
                    # 如果是单参数，直接传递
                    elif len(params) == 1:
                        result = func(input_data)
                    else:
                        result = func(action_input)
                except json.JSONDecodeError:
                    # JSON 解析失败，按单参数处理
                    if len(params) == 1:
                        result = func(action_input)
                    else:
                        result = func(action_input)

                observation = f"Observation: {result}"

                messages.append({"role": "assistant", "content": response})
                messages.append({"role": "user", "content": observation})

            else:
                return "Unknown action"