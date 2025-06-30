# import os
# os.
# 上面两句能验证python/pylance插件的代码补齐功能

# import sys
# 上面一行Ruff代码检查验证
# import sys 这行代码下方应该会出现黄色的波浪线，当您把鼠标悬停在上面时，会提示 F401: 'sys' imported but unused。

# x   =   10
# 上面一行验证Ruff自动格式化，保存后会自动变为x = 10

# name: str = "Alice"
# name = 123
# 上面两行 验证Mypy静态类型检查，保存后123会出现红色波浪线，报错
# Incompatible types in assignment (expression has type "int", variable has type "str")

# * 这是重要的绿色注释
# ! 这是危险的红色注释
# ? 这是疑问的蓝色注释
# TODO: 这是待办的橙色注释
# 上面四行验证better comments

# def greet(name: str) -> None:
#    """ # <--- 在这里输入三个引号后按回车
# 验证autoDocstring


def greet(name: str) -> None:
    """_summary_

    Args:
        name (str): _description_
    """


# 验证gitLens
# 打开一个已经被Git提交过的文件（比如您之前修改过的 hello_world.py）。用鼠标光标点击任意一行代码。
# 预期结果: 在该行的末尾，应该会出现一行灰色的半透明文字，显示着类似 You, 2 hours ago... 的提交信息。
