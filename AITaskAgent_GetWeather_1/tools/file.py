from pathlib import Path

def write_file(filename, content):
    """
    写入文件内容

    :param filename: 文件名
    :param content: 文件内容
    :return: 写入成功提示
    """
    file_path = Path(__file__).parents[1] / "files" / filename
    # 确保文件所在目录存在
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content + "\n")

    return "File written successfully"