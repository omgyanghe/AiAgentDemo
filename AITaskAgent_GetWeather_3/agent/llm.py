import os
from openai import OpenAI
import dotenv
from schemas.tool_schemas import tools_schema

dotenv.load_dotenv()

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),  # 填写DashScope SDK的base_url
)

def call_llm(messages):
    """
    调用LLM模型

    :param messages: 消息列表，每个消息是一个字典，包含"role"和"content"键
    :return: LLM模型的响应
    """
    completion = client.chat.completions.create(
        model="qwen3-max-2026-01-23",
        messages=messages,
        tools=tools_schema,
    )

    return completion
    # return completion.choices[0].message.content
    # return completion.model_dump_json()

if __name__ == "__main__":
    messages = [
        {"role": "user", "content": "帮我查 Los Angeles 天气，并保存到 weather.txt"}
    ]
    response = call_llm(messages)
    print(response)