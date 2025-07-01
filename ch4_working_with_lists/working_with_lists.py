magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

# For循环遍历列表

# for cat in cats:
# for dog in dogs:
# for item in list_of_items:
# 单数-复数写法更有可读性

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")


# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)
# IndentationError: expected an indented block after 'for' statement on line 30
# 忘记缩进错误，位于 for 语句后面且属于循环组成部分的代码行，一定要缩进。

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
# 忘记缩进额外的代码行,没有达到预期的功能，存在逻辑错误

# message = "Hello Python world!"
#     print(message)
# 不必要的缩进，报错IndentationError: unexpected indent
# 为避免意外的缩进错误，请只缩进需要缩进的代码。

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you everyone, that was a great magic show!")
# 缩进了循环后的代码 也是逻辑错误

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians
#   print(magician)
# for 语句末尾的冒号告诉 Python，下一行是循环的第一行。
# 报错，SyntaxError: expected ':'

# Python 函数 range() 让你能够轻松地生成一系列的数。
for value in range(1, 5):
    print(value)
# 打印1, 2, 3, 4
# 输出不包含第二个值
for value in range(1, 6):
    print(value)

# 在调用 range() 函数时，也可只指定一个参数，这样它将从 0 开始
for value in range(6):
    print(value)

# 要创建数值列表，可使用 list() 函数将 range() 的结果直接转换为列表。
# 如果将 range() 作为 list() 的参数，输出将是一个数值列表。
numbers = list(range(1, 6))
print(numbers)

# 在使用 range() 函数时，还可指定步长。为此，可以给这个函数指定第三个参数，Python 将根据这个步长来生成数。
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)
# range() 函数返回的不是一个列表（list），而是一个特殊的、不可变的**range对象**。
# 这个range对象，是一个可迭代对象（iterable）。
# range(1, 100)，如果是list，计算机会把100个都存储起来
# 但对于range对象，计算机在内存中只存储了三个数字：起始值（0）、结束值（10000）和步长（默认为1）。它并没有生成那10000个数字。
# 这个range对象非常懒惰和节约内存资源，只记录了生成数字的规则
# 虽然它不是列表，但它的行为在很多方面和列表非常相似
# 它是“可迭代的”（Iterable）：
# 这意味着您可以把它放在for循环里。当for循环向range对象要下一个数时，range对象会根据它内部的“公式”（起始值、结束值、步长）实时计算出下一个数并交出来，然后等待下一次的请求。
# 它支持常见的序列操作（而且效率很高）
# len(range(0,100)) = 100，且时间复杂度为O(1)，只需100 - 1，不需要去数
# 50 in range(0, 100)结果为True，时间复杂度O(1),数学判断不需要遍历元素
# range(0, 100)[50]结果为50，复杂度为O(1)，因为是计算出来的

# range() 在使用上像一个列表，但在实现上却是一个高效的、即时计算的数字序列生成器。它用固定的、极小的内存空间，就能表示一个可能包含亿万个数字的序列，从而极大地节省了内存。

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表推导式(List Comprehensions)
# 列表推导式将 for 循环和创建新元素的代码合并成一行，并自动追加新元素。
squares = [value**2 for value in range(1, 11)]
print(squares)
# 要使用这种语法，首先指定一个描述性的列表名，如 squares。然后指定一个左方括号，并定义一个表达式，
# 用于生成要存储到列表中的值。在这个示例中，表达式为 value**2，它计算平方值。接下来，编写一个 for 循环，
# 用于给表达式提供值，再加上右方括号。在这个示例中，for 循环为 for value in range(1,11)，
# 它将值 1～10 提供给表达式 value**2。请注意，这里的 for 语句末尾没有冒号。


# 切片用于处理列表的部分而不是全部元素
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
# 与range() 函数一样，Python 在到达指定的第二个索引之前的元素时停止。不包括第二个索引元素
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
# 切片也是一个列表
# 你可以生成列表任意子集
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:4])

# 如果没有指定第一个索引，Python 将自动从列表开头开始
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[:4])

# 省略终止索引，自动终止于列表末尾
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[2:])

# 索引也可以是负数，代表倒数第几个
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:-1])  # 从第一个开始，不包括倒数第一个

# 索引也可以是负数，代表倒数第几个
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[-2:-1])
# 从倒数第二个开始，不包括倒数第一个 倒数第二个结束，输出只有一个元素的列表

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[3:2])  # 输出空列表

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[-3:])
# 无论列表怎么变化 输出最后三个元素

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[::2])
# 可在表示切片的方括号内指定第三个值。这个值告诉 Python在指定范围内每隔多少元素提取一个。
# 从开头到结尾，两个元素一个

# Python 中切片的完整语法是 a[start:stop:step]，它从一个序列（如列表、字符串、元组）中提取出一个新的子序列。
# start: 切片开始的索引。新的子序列会包含这个位置的元素。
# stop: 切片结束的索引。新的子序列会不包含这个位置的元素。
# step: 步长，即每一步跳跃的距离。
# Python 会根据 step 的正负来智能地设定省略时的默认值。
# 当 step 为正数时（或省略，默认为 1）—— 从左向右
# a[start:stop] (省略 step): 步长默认为 1，即一个挨一个地取。
# a[:stop] (省略 start): start 默认为 0，表示从列表的开头开始。
# a[start:] (省略 stop): stop 默认为列表的长度，表示一直取到列表的最后一个元素。
# a[:]: 省略 start 和 stop，表示从头到尾，完整地复制整个列表。
# 当 step 为负数时 —— 从右向左（这是理解反转的关键）
# 当步长为负数时，切片的方向会反过来，默认值也会相应地改变。
# a[start:stop:-1]：表示从 start 开始，每次向前（向左）移动一个位置，直到 stop。
# a[:stop:-1] (省略 start): start 默认为 -1，即列表的最后一个元素。
# a[start::-1] (省略 stop): stop 默认为列表的开头之前的位置，以确保能取到第一个元素。
# a[::-1]: 这是最常用的反转写法。start 默认为最后一个元素，stop 默认为开头之前，step 为 -1。完整含义就是：“从最后一个元素开始，一个一个地向前取，直到取完所有元素为止。”
# 切片操作会从 start 索引开始，以 step 为步长，提取元素，直到 stop 索引之前停止。stop 索引本身永远不会被包含在结果中。
# 情况一：step 为正数（或省略，默认为 +1）
# 此时，切片方向为从左到右。
# start 省略时：默认值为 0，即从列表的第一个元素开始。
# stop 省略时：默认值为列表的长度 len(a)，即切片会一直持续到并包含列表的最后一个元素。
# 情况二：step 为负数
# 此时，切片方向为从右向左。
# start 省略时：默认值为 -1 (或 len(a) - 1)，即从列表的最后一个元素开始。
# stop 省略时：默认值为列表的开头之前的位置。为了能包含索引为 0 的第一个元素，切片必须在它“左边”的位置停止，所以这个默认值可以理解为 -len(a) - 1。
# 如果没有提取到任何元素，返回空列表。


# 如果要遍历列表的部分元素，可在 for 循环中使用切片。
players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 在很多情况下，切片是很有用的。例如，在编写游戏时，可以在玩家退出游戏时将其最终得分加入一个列表，
# 然后将该列表按降序排列，再创建一个只包含前三个得分的切片，以获取该玩家的三个最高得分；
# 在处理数据时，可以使用切片来进行批量处理；在编写 Web 应用程序时，
# 可以使用切片来分页显示信息，并在每页上显示数量合适的信息。


# 列表复制，根据已有列表创建新列表。
# 要复制列表，可以创建一个包含整个列表的切片
# 方法是同时省略起始索引和终止索引([:])
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# 切片产生了独立的新list,创建了副本


my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
# 赋值只是让两个变量指向同一个list
