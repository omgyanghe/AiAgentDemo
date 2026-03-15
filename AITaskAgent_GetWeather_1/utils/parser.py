import re

def parse_action(text):
    # 使用字符类 [：:] 同时匹配中文和英文冒号，因为在不同语言环境下，冒号的表示方式可能不同
    action = re.search(r"Action[：:]\s*(.*)", text)
    action_input = re.search(r"Action Input[：:]\s*(.*)", text)

    if action and action_input:
        return action.group(1), action_input.group(1)

    return None, None