# 大多数程序旨在解决最终用户的问题，因此通常需要从用户那里获取输入。
# 在本章中，将学习如何接受用户输入，让程序对其进行处理。
# 当程序需要一些信息时，需要提示用户输入这些信息。
# 学习如何在需要时让程序不断地运行，以便用户输入尽可能多的信息，然后在程序中使用这些信息。
# 为此，将使用 while 循环让程序不断地运行，直到指定的条件不再满足为止。
# 通过获取用户输入并学会控制程序的运行时间，就能编写出交互式程序。


# input() 函数让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python 将其赋给一个变量，以便使用。
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# input() 函数接受一个参数，即要向用户显示的提示（prompt），让用户知道该输入什么样的信息。
# 程序等待用户输入，并在用户按回车键后继续运行。用户的输入被赋给变量message。
# Python 的 input() 函数在接收到换行符（newline character） 时就会结束等待，并继续执行后面的代码。
# 这个换行符通常是在用户在键盘上按下回车键 (Enter/Return) 时被发送到程序中的。

# 每当使用 input() 函数时，都应指定清晰易懂的提示，准确地指出希望用户提供什么样的信息。
# 通过在提示末尾（这里是冒号后面）添加一个空格，可将提示与用户输入分开。
name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!")

# 有时候，提示可能超过一行。例如，你可能需要指出获取特定输入的原因。
# 在这种情况下，可先将提示赋给一个变量，再将这个变量传递给 input()函数。
# Python 中的两个（或多个）字符串可以直接使用加号 + 进行相加。
# 这个操作叫做 “字符串拼接” (String Concatenation)。它会把两个字符串首尾相连，生成一个全新的字符串。
# 下面展示了创建多行字符串的方式。
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name.title()}!")

# 在使用 input() 函数时，Python 会将用户输入解读为字符串。
age = input("How old are you? ")
print(type(age))
# print(age >= 18)
# TypeError: '>=' not supported between instances of 'str' and 'int'
# Python无法将字符串与数值进行比较。


# 为了解决这个问题，可使用函数 int() 将输入的字符串转换为数值，确保能够成功地执行比较操作。
age = input("How old are you? ")
age_int = int(age)
print(age_int >= 18)
# int() 将这个字符串转换成了数值表示。这样 Python 就能运行条件测试了。
input_height = input("How tall are you, in inches? ")
height = int(input_height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


# 在处理数值信息时，求模运算符（%）是个很有用的工具，它将两个数相除并返回余数：
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)
# 如果一个数可被另一个数整除，余数就为 0，因此求模运算将返回 0。可利用这一点来判断一个数是奇数还是偶数：
number_input = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number_input)
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# 上面这样写也能正常运行，但是mypy的静态类型检查会报错。
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
