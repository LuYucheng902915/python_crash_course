"This is a string."

"This is also a string."
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

name = "ada lovelace"
print(name.title())  # name.title() 返回一个新字符串，原字符串不变
# name.title() 本身不是一个变量，而是一个 表达式（Expression）。
# Python会首先对这个表达式求值（Evaluate），得到它的返回值（Return Value）。
# 然后，这个返回值被作为参数传递给外层的 print() 函数。
print(name)  # 字符串是不可变的，输出仍然是 "ada lovelace"

titled_name = name.title()  # 将返回的新字符串用新变量保存
print(titled_name)  # 输出 "Ada Lovelace"

name = "ada lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
# 这种字符串称为 f 字符串。f 是 format（设置格式）的简写，
# 因为Python 通过把花括号内的变量替换为其值来设置字符串的格式。

print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

# 在编程中，空白（Whitespace）泛指任何非打印字符，如空格、制表符和换行符。
# 你可以使用空白来组织输出，让用户阅读起来更容易。

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = "python "
favorite_language
favorite_language.rstrip()  # 删除末尾的空格,但不会改变字符串
favorite_language  # 输出仍然是 "python "
favorite_language = favorite_language.rstrip()  # 将删除空格后的字符串赋值给变量
favorite_language  # 输出 "python"
# 上面六句要在解释器中能看出效果

favorite_language = " python "
favorite_language.rstrip()
favorite_language.lstrip()  # 删除开头的空格
favorite_language.strip()  # 删除开头和末尾的空格
# 上面三句要在解释器中能看出效果

nostarch_url = "https://nostarch.com"
nostarch_url.removeprefix("https://")  # 删除前缀，不改变原字符串
simple_url = nostarch_url.removeprefix("https://")  # 保存删除的结果到新变量
simple_url
# 上面四句要在解释器中能看出效果
# 类似的还有removesuffix()方法，用于删除字符串末尾的后缀。

message = "one of Python's strengths is its diverse and supportive community."
print(message)


# message = 'one of Python's strengths is its diverse and supportive community.'
# SyntaxError: unterminated string literal (detected at line 67)
# 上面这句会报错，因为字符串中的单引号与字符串的开始和结束引号冲突了。
# 错误发生在最后一个单引号后面
# 解决方法是使用双引号来定义字符串，或者在单引号前加上反斜杠（\）来转义它。

message = "one of Python's strengths is its diverse and supportive community."
print(message)
# message = 'one of Python\'s strengths is its diverse and supportive community.'
# 上面这句也是正确的，但是保存后会被使用的格式工具修改格式成双引号
