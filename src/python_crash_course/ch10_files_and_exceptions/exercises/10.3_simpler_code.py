# 10-3. Simpler Code:
# The program file_reader.py in this section uses a temporary variable, lines, to show how splitlines() works.
# You can skip the temporary variable and loop directly over the list that splitlines() returns:
# for line in contents.splitlines():
# Remove the temporary variable from each of the programs in this section, to make them more concise.

from pathlib import Path

path = Path("../pi_digits.txt")

for line in path.read_text().splitlines():
    print(line)

path = Path("../pi_million_digits.txt")

pi_string = ""
for line in path.read_text().splitlines():
    pi_string += line.strip()

print(pi_string[:52])
print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# 调试代码时，VS Code 会把代码运行在 “调试控制台” (DEBUG CONSOLE) 中。
# 这个控制台的主要作用是显示程序的输出 (print 的内容) 和调试信息。它不是一个交互式环境，无法接收来自 input() 函数的请求。
# 如果直接对需要输入的程序按 F5 开始调试，程序就会卡在 input() 那里。
# 可以在启动配置 (launch.json) 文件里，把运行环境从 "internalConsole" (调试控制台) 改成 "integratedTerminal" (集成终端)。
# 这样，调试就会可以输入的终端窗口里进行了。
# 此外 VS Code 在复用终端，有时候有 bug，会导致将命令行输入的命令作为程序的输入。
# 具体来说，点击右上方快捷键，在专用终端中运行 Python 文件。
# 如果之前已经打开过专用终端，VS Code 会复用这个终端，导致后续的 input() 函数可能直接读取到残留的命令，而不是等待用户正常输入。
# print(f"\n{birthday}")
# cd /home/luyucheng/learning/python-learning/python-crash-course/ch10_files_and_exceptions/exercises
# 但是直接在终端执行同样的命令，就可以正常输入。
# 最好的方法就是在终端中输入命令运行需要用户输入的 Python 文件。
# 空字符串 in 任何字符串的结果一定是 True。
# 在 Python (以及许多其他编程语言) 中，in 操作符用于检查一个字符串是否是另一个字符串的子字符串 (substring)。
# 语言设计的逻辑是：一个空字符串可以被认为存在于任何字符串的任何位置（包括开头、结尾和任意两个字符之间）。
# 因为它不需要任何字符来匹配，所以它总是能“匹配”成功。
