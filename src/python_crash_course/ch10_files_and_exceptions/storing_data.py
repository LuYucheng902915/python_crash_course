# 存储数据。很多程序要求用户输入某种信息，比如让用户存储游戏首选项或提供要可视化的数据。
# 不管专注点是什么，程序都会把用户提供的信息存储在列表和字典等数据结构中。
# 当用户关闭程序时，几乎总是要保存他们提供的信息。一种简单的方式是使用模块 json 来存储数据。
# 模块 json 能够将简单的 Python 数据结构转换为 JSON 格式的字符串，并在程序再次运行时从文件中加载数据。
# 还可以使用 json 在 Python程序之间共享数据。
# 更重要的是，JSON 数据格式并不是 Python 专用的，能够将以 JSON 格式存储的数据与使用其他编程语言的人共享。
# 这是一种轻量级数据格式，不仅很有用，也易于学习。
# 注意：JSON（JavaScript Object Notation）格式最初是为 JavaScript 开发的，但随后成了一种通用的格式，被包括 Python 在内的众多语言采用。
# 尽管它的名字里有 "JavaScript"，但它实际上是一种独立于任何编程语言的、纯文本格式，专门用于存储和交换数据。
# 可以把它想象成一种国际通用的“数据护照”或“集装箱”。
# 无论数据来自哪种编程语言（Python, Java, C++, Go...），只要把它打包成 JSON 这种标准格式，任何其他语言都能轻松地打开并准确地读出里面的内容，不会有任何误解。
# 对机器友好：结构严谨，有统一的解析规则，程序可以非常快速、无歧义地进行读写。
# 对人类友好：它就是纯文本，结构清晰，人类也能轻松阅读和编辑。

# JSON 的基本结构与数据类型，JSON 的结构只有两种：
# 对象 (Object)：由大括号 {} 包裹。里面是一系列无序的 “键/值”对 (key/value pairs)。
# 键必须是字符串，值可以是任何 JSON 支持的数据类型。这就像 Python 里的字典。
# 数组 (Array)：由方括号 [] 包裹。里面是一系列有序的值。值之间用逗号分隔。这就像 Python 里的列表。
# JSON 支持以下几种基本数据类型：
# 字符串 (String)：必须用双引号 "" 包裹。
# 数字 (Number)：整数或浮点数，不带引号。
# 布尔值 (Boolean)：true 或 false。注意是全小写。
# 数组 (Array)：[...]，可以嵌套。
# 对象 (Object)：{...}，可以嵌套。
# null：表示空值。也是小写。
# 数组或对象的最后一个元素后面不能有逗号。
# 不允许任何形式的注释。
# 一个标准的 JSON 文本，其最外层（根部）必须是且仅是 一个 有效的 JSON 值。它不能是多个值的并列。
# 文件内容就是一个完整的对象，文件内容就是一个完整的数组，文件内容就是一个字符串，都是合法的 JSON文件。

import json
from pathlib import Path

# 下面先编写一个存储一组数的简短程序，再编写一个将这些数读取到内存中的程序。
# 第一个程序将使用 json.dumps() 来存储这组数，而第二个程序将使用 json.loads() 来读取它们。
# json.dumps() 函数接受一个实参，即要转换为 JSON 格式的数据。
# 这个函数返回一个字符串，这样就可将其写入数据文件了。
numbers = [2, 3, 5, 7, 11, 13]
path = Path("numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)
# 首先导入模块 json，并创建一个数值列表。
# 然后选择一个文件名，指定要将该数值列表存储到哪个文件中。
# 通常使用文件扩展名 .json 来指出文件存储的数据为 JSON 格式。
# 接下来，使用 json.dumps() 函数生成一个字符串，它包含我们要存储的数据的 JSON 表示形式。
# 生成这个字符串后，像本章前面一样，使用 write_text() 方法将其写入文件。
# 下面再编写一个程序，使用 json.loads() 将这个列表读取到内存中：
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
# 确保读取的是前面写入的文件。
# 这个数据文件是使用特殊格式的文本文件，因此可使用 read_text() 方法来读取它。
# 然后将这个文件的内容传递给 json.loads()。
# 这个函数将一个 JSON 格式的字符串作为参数，并返回一个 Python 对象（这里是一个列表），将这个对象赋给了变量 numbers。
# 最后，打印恢复的数值列表，看看是否与之前的数值列表相同。
# 这是一种在程序之间共享数据的简单方式。

# 保存和读取用户生成的数据：使用 json 保存用户生成的数据很有必要，因为如果不以某种方式进行存储，用户的信息就会在程序停止运行时丢失。
# 下面来看一个这样的例子：提示用户在首次运行程序时输入自己的名字，并且在他再次运行程序时仍然记得他。
# 先来存储用户的名字：
username = input("What is your name? ")
path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")
# 首先，提示用户输入名字。接下来，将收集到的数据写入文件 username.json。然后，打印一条消息，指出存储了用户输入的信息。
# 现在向名字已被存储的用户发出问候：
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")
# 读取数据文件的内容，并使用 json.loads() 将恢复的数据赋给变量 username。
# 有了已恢复的用户名，就可以使用个性化的问候语欢迎用户回来了。
# 需要将这两个程序合并到一个程序中。
# 在这个程序运行时，将尝试从文件中获取用户的用户名。
# 如果没有找到，就提示用户输入用户名，并将其存储到文件 username.json 中，以供下次使用。
# 这里原本可以编写一个 try-except 代码块，以便在文件 username.json 不存在时采取合适的措施，但没有这样做，而是使用了 pathlib 模块提供的一个便利方法。
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    user_name = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
# Path 类提供了很多很有用的方法。
# 如果指定的文件或文件夹存在，exists() 方法返回 True，否则返回 False。
# 这里使用 path.exists() 来确定是否存储了用户名。
# 如果文件 username.json 存在，就加载其中的用户名，并向用户发出个性化问候。
# 如果文件 username.json 不存在，就提示用户输入用户名，并存储用户输入的值。
# 无论执行的是哪个代码块，都将显示用户名和合适的问候语。


# 重构：经常会遇到这样的情况：虽然代码能够正确地运行，但还可以将其划分为一系列完成具体工作的函数来进行改进。
# 这样的过程称为重构。重构让代码更清晰、更易于理解、更容易扩展。
# 要重构上面的代码，可将其大部分逻辑放到一个或多个函数中。
# 该代码的重点是问候用户，因此将其所有代码都放到一个名为 greet_user() 的函数中。
def greet_user():
    """
    问候用户，并指出其名字
    """
    path = Path("username.json")
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")


greet_user()


# 考虑到现在使用了一个函数，我们删除注释，转而使用一个文档字符串来指出程序的作用。
# 这个程序更加清晰，但 greet_user() 函数所做的不仅是问候用户，还在存储了用户名时获取它，在没有存储用户名时提示用户输入。
# 首先将获取已存储用户名的代码移到另一个函数中。
def get_stored_username(path):
    """
    如果存储了用户名，就获取它
    """
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def greet_user_refactor1():
    """
    问候用户，并指出其名字
    """
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")


greet_user_refactor1()
# 新增的 get_stored_username() 函数目标明确，文档字符串指出了这一点。
# 如果存储了用户名，就获取并返回它；如果传递给 get_stored_username() 的路径不存在，就返回 None。
# 这是一种不错的做法：函数要么返回预期的值，要么返回 None。
# 这使得能够使用函数的返回值做简单的测试。
# 如果成功地获取了用户名，就打印一条欢迎用户回来的消息，否则提示用户输入用户名。


# 还需要将 greet_user() 中的另一个代码块提取出来，将在没有存储用户名时提示用户输入的代码放在一个独立的函数中：
def get_new_username(path):
    """
    提示用户输入用户名
    """
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user_refactor2():
    """
    问候用户，并指出其名字
    """
    path = Path("username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


greet_user_refactor2()
# 在个最终版本中，每个函数都执行单一而清晰的任务。
# 调用 greet_user()，它打印一条合适的消息：要么欢迎老用户回来，要么问候新用户。
# 为此，它首先调用 get_stored_username()，这个函数只负责获取已存储的用户名（如果存储了），再在必要时调用 get_new_username()，这个函数只负责获取并存储新用户的用户名。
# 要编写出清晰且易于维护和扩展的代码，这种划分必不可少。
