message = "Hello Python world!"
print(message)
# 添加了一个名为 message 的变量（variable）。每个变量指向一个值（value）——与该变量相关联的信息。
# 在这里，指向的值为字符串"Hello Python world!"。

message = "Hello Python Crash Course world!"
print(message)
# 在程序中，可随时修改变量的值，而 Python 将始终记录变量的最新值。

# 编辑器将代码不同部分显示成不同颜色称为语法高亮。

# 变量名只能包含字母、数字和下划线 。变量名能以字母或下划线打头，变量名不能以数字打头。
# 变量名不能包含空格，但能使用下划线来分隔其中的单词。
# 不要将 Python 关键字和函数名用作变量名。变量名应既简短又具有描述性。
# 慎用小写字母 l 和大写字母 O，因为它们可能被人错看成数字 1 和 0。
# 应使用小写的 Python 变量名。虽然在变量名中使用大写字母不会导致错误，但大写字母在变量名中有特殊的含义。
# 在 Python 3 中，变量名还可以包含其他 Unicode 字符。例如，中文字符也是支持的，但是不推荐。

# message = "Hello Python Crash Course reader!"
# print(mesage)
# NameError: name 'mesage' is not defined. Did you mean: 'message'?
# 如果程序无法成功地运行，解释器将提供一个 traceback。traceback 是一条记录，指出了解释器在尝试运行代码时，在什么地方陷入了困境。
# 名称错误通常意味着两种情况：要么在使用变量前忘记了给它赋值，要么在输入变量名时拼写不正确。

mesage = "Hello Python Crash Course reader!"
print(mesage)
# Python 解释器不会对代码做拼写检查，但要求变量名的拼写一致。
# 变量名是一致的，因此在 Python 看来，这不是问题。编程语言要求严格，但不关心拼写是否正确。

# 变量是可以被赋值的标签，也可以说变量指向特定的值（对象），或者说变量是对象的引用。
# “是引用/标签” 是一种更高层、更抽象的描述。它完全屏蔽了“地址”这个具体的实现细节。它只关心一件事：变量名和对象之间的指向关系。

x = 10
y = x
# id() 函数可以获取对象的内存地址，可以看作是对象的唯一身份证号。
print(f"x 指向的对象ID: {id(x)}")
print(f"y 指向的对象ID: {id(y)}")
print(f"x 和 y 指向同一个对象吗? {id(x) == id(y)}")

x = 10
y = x
print(f"操作前, y 的值是: {y}")  # y 是 10
x = 20  # 把 x 标签移动到新对象 20 上
print(f"操作后, x 的值是: {x}")  # x 是 20
print(f"操作后, y 的值是: {y}")  # y 仍然是 10
print(f"现在 x 和 y 指向同一个对象吗? {id(x) == id(y)}")  # False
