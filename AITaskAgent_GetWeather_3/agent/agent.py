from cgitb import text
import json
from agent.llm import call_llm
from tools.registry import TOOLS

class Agent:

    def run(self, user_input):

        messages = [
            {"role": "user", "content": user_input}
        ]

        while True:

            response = call_llm(messages)

            message = response.choices[0].message

            # 如果没有工具调用
            if not message.tool_calls:
                return message.content

            # 记录助手的工具调用
            # 为什么要记录？因为助手的工具调用会改变消息的内容，后续的消息需要包含助手的工具调用
            messages.append(message)

            # 执行工具
            for tool_call in message.tool_calls:

                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)

                result = TOOLS[name](**args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })

# 帮我查一下Beijing的天气，并将信息保存在weather.txt文件中。