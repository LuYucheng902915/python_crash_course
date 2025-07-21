# 第一种数据类型：字符串。
# 字符串是一系列字符，用引号引起的都是字符串，其中的引号可以是单引号，也可以是双引号。
"This is a string."

"This is also a string."
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
# 上面是一些字符串的例子。引号的灵活性使得字符串中可以包含引号和撇号。

name = "Ada lovelace"
print(name.title())
# title() 方法出现在这个变量的后面。方法(method)是 Python 可对数据执行的操作。
# 在 name.title() 中，name后面的句点（.）让 Python 对 name 变量执行 title() 方法指定的操作。
# title() 函数不需要额外的参数，因此它后面的括号是空的。
# title() 方法以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写，后面的字母改为小写。
# name.title() 返回一个新字符串，原字符串不变。
# name.title() 本身不是一个变量，而是一个表达式（Expression）。
# Python会首先对这个表达式求值（Evaluate），得到它的返回值（Return Value）。
# 然后，这个返回值被作为参数传递给外层的 print() 函数。

print(name)
# 字符串是不可变的，输出仍然是 "ada lovelace"。

titled_name = name.title()  # 将返回的新字符串用新变量保存
print(titled_name)  # 输出 "Ada Lovelace"

name = "ada lovelace"
print(name.upper())
print(name.lower())
# 将字符串改为全大写/全小写。
# 存储数据往往把数据改成全小写再存储。


# 在字符串中使用变量。
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
# 这种字符串称为 f 字符串。f 是 format（设置格式）的简写，因为Python 通过把花括号内的变量替换为其值来设置字符串的格式。
# f-字符串里的 {} 会自动对其中的任何非字符串变量或表达式调用其 __str__() 方法。
# 而是Python面向对象设计中的一个约定。几乎所有的Python内置对象（如整数int、浮点数float、列表list、布尔值bool等）都有一个名为 __str__() 的特殊方法。
# 这个方法的任务就是返回一个“对用户友好的”、适合打印的字符串表示。
# 使用 f 字符串可以完成很多任务，如利用与变量关联的信息来创建完整的消息。

print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)


# 使用制表符/换行符添加空白。
# 在编程中，空白（Whitespace）泛指任何非打印字符，如空格、制表符和换行符。
# 你可以使用空白来组织输出，让用户阅读起来更容易。

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# 字符串 "\n\t" 让Python 换到下一行，并在下一行开头添加一个制表符。


# 删除字符串中多余的空白。
favorite_language = "python "
favorite_language
favorite_language.rstrip()  # 删除末尾的空格，但不会改变字符串
favorite_language  # 输出仍然是 "python "
favorite_language = favorite_language.rstrip()
# 将删除空格后的字符串赋值给变量，才能永久删除空白。
# 在编程中，经常需要修改变量的值，再将新值关联到原来的变量。
favorite_language  # 输出 "python"
# 上面六句要在解释器中能看出效果，解释其中询问变量的值，可以看到右边的空白。

favorite_language = " python "
favorite_language.rstrip()
favorite_language.lstrip()  # 删除开头的空格
favorite_language.strip()  # 删除开头和末尾的空格
# 上面三句要在解释器中能看出效果。
# 在实际程序中，这些函数最常用于在存储用户输入前对其进行清理。

nostarch_url = "https://nostarch.com"
nostarch_url.removeprefix("https://")  # 删除前缀，不改变原字符串
simple_url = nostarch_url.removeprefix("https://")  # 保存删除的结果到新变量
simple_url
# 字符串删除前缀的方法removeprefix(要删除的前缀字符串)。
# 该函数同样不会改变原来的字符串。
# 。如果想保留删除前缀后的值，既可将其重新赋给原来的变量，也可将其赋给另一个变量。
# 上面四句要在解释器中能看出效果。
# 类似的还有removesuffix()方法，用于删除字符串末尾的后缀。


# 当程序包含非法的 Python 代码时，就会导致语法错误。例如，在用单引号引起的字符串中包含撇号，就将导致错误。
# 这是因为这会导致 Python 将第一个单引号和撇号之间的内容视为一个字符串，进而将余下的文本视为 Python 代码，从而引发错误。
message = "one of Python's strengths is its diverse and supportive community."
print(message)
# 撇号位于两个双引号之间，因此 Python 解释器能够正确地理解这个字符串。

# message = 'one of Python's strengths is its diverse and supportive community.'
#   message = 'one of Python's strengths is its diverse and supportive community.'
#                                                                                ^
# 语法错误发生在最后一个单引号后面。在解释器看来，这种语法错误表明一些内容不是有效的 Python 代码。
# SyntaxError: unterminated string literal (detected at line 67)
# 上面这句会报错，因为字符串中的单引号与字符串的开始和结束引号冲突了。
# 错误发生在最后一个单引号后面。
# 解决方法是使用双引号来定义字符串，或者在单引号前加上反斜杠（\）来转义它。
# 编辑器的语法高亮功能可帮助你快速找出某些语法错误。
# 如果看到 Python 代码以普通句子的颜色显示，或者普通句子以Python代码的颜色显示，就可能意味着文件中存在引号不匹配的情况。


message = "one of Python's strengths is its diverse and supportive community."
print(message)
# message = 'one of Python\'s strengths is its diverse and supportive community.'
# 上面这句也是正确的，但是保存后会被使用的格式工具修改格式成双引号。
