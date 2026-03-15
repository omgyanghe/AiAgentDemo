import os
from openai import OpenAI
import dotenv

from prompt import SYSTEM_PROMPT

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
        messages=messages
    )

    return completion.choices[0].message.content
    # return completion.model_dump_json()