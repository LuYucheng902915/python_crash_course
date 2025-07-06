# for 循环用于针对集合中的每个元素执行一个代码块，而 while 循环则不断地运行，直到指定的条件不再满足为止。


# 可以用while循环计数。
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 游戏使用 while 循环，确保在玩家想玩时不断运行，并在玩家想退出时结束运行。

# 可以使用 while 循环让程序在用户愿意时不断地运行，在代码中定义了一个退出值，只要用户输入的不是这个值，程序就将一直运行。
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)
    print(message)
# Python 在首次执行 while语句时，需要将 message 的值与 'quit' 进行比较，但此时用户还没有输入。
# 如果没有可供比较的东西，Python 将无法继续运行程序。为解决这个问题，必须给变量 message 指定初始值。
# 虽然这个初始值只是一个空字符串，但符合要求，能够让 Python 执行 while 循环所需的比较。

# 这个程序很好，唯一美中不足的是，它将单词 'quit' 也作为一条消息打印了出来。为了修复这种问题，只需要使用一个简单的 if 测试：
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)
# 仅当消息不是退出值才打印。

# 使用标志，在上一个示例中，让程序在满足指定条件时执行特定的任务。但在更复杂的程序中，有很多不同的事件会导致程序停止运行。
# 当导致程序结束的事件有很多时，如果在一条while 语句中检查所有这些条件，将既复杂又困难。
# 在要求满足很多条件才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。
# 这个变量称为标志（flag），充当程序的交通信号灯。
# 可以让程序在标志为 True 时继续运行，并在任何事件导致标志的值为 False 时让程序停止运行。
# 这样，在 while 语句中就只需检查一个条件：标志的当前值是否为 True。
# 然后将所有测试（是否发生了应将标志设置为False 的事件）都放在其他地方，从而让程序更整洁。
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)
# 标志active用于判断程序是否应该继续运行。
# 将变量 active 设置为 True，让程序最初处于活动状态。
# 这样做简化了while 语句，因为不需要在其中做任何比较——相关的逻辑由程序的其他部分处理。
# 只要变量 active 为 True，循环就将一直运行。
# 在 while 循环中，在用户输入后使用一条 if 语句检查变量 message的值。
# 如果用户输入的是 'quit'，就将变量 active 设置为 False，这将导致 while 循环不再继续执行。
# 如果用户输入的不是 'quit'，就将输入作为一条消息打印出来。
# 这个程序的输出与上一个示例相同。
# 上一个示例将条件测试直接放在了while 语句中，而这个程序则使用一个标志来指出程序是否处于活动状态。

# 这样，添加测试（如 elif 语句）以检查是否发生了其他导致 active 变为False 的事件，就会很容易。
# 在复杂的程序（比如有很多事件会导致程序停止运行的游戏）中，标志很有用：在任意一个事件导致活动标志变成 False时，主游戏循环将退出。
# 此时可显示一条游戏结束的消息，并让用户选择是否要重玩。


# 如果不管条件测试的结果如何，想立即退出 while 循环，不再运行循环中余下的代码，可使用 break 语句。
# break 语句用于控制程序流程，可用来控制哪些代码行将执行、哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")
# 以 while True 打头的循环将不断运行，直到遇到 break 语句。
# 这个程序中的循环不断地让用户输入他到过的城市的名字，直到用户输入'quit' 为止。
# 在所有 Python 循环中都可使用 break 语句。例如，可使用break 语句来退出遍历列表或字典的 for 循环。
# Python 的 break 语句只会终止其所在的、最内层的那一级循环。
# 如果存在多层嵌套循环，break 不会影响到外层循环的执行，外层循环会继续它的下一次迭代。


# 要返回循环开头，并根据条件测试的结果决定是否继续执行循环，可使用continue 语句，它不像 break 语句那样不再执行余下的代码并退出整个循环。
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# 只打印奇数。
# 如果结果为 0（意味着 current_number 可被 2 整除），就执行 continue 语句，让 Python 忽略余下的代码（不打印），并返回循环的开头。
# 如果当前的数不能被 2 整除，就执行循环中余下的代码，将这个数打印出来。

# 每个 while 循环都必须有结束运行的途径，这样才不会没完没了地执行下去。
x = 1
while x <= 5:
    print(x)
    x += 1
# 下面这个循环将没完没了地运行。
# 可以按Ctrl + C或者关闭终端。
# x = 1
# while x <= 5:
#     print(x)
# 要避免编写无限循环，务必对每个 while 循环进行测试，确保它们按预期那样结束。
# 如果希望程序在用户输入特定值时结束，可运行程序并输入该值。
# 如果程序在这种情况下没有结束，请检查程序处理这个值的方式，确认程序至少有一个地方导致循环条件为 False 或导致 break 语句得以执行。
