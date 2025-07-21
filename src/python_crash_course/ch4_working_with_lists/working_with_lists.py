# 将学习如何遍历整个列表，无论列表有多长，都只需要几行代码就能做到。
# 循环让你能够对列表的每个元素采取一个或一系列相同的措施，从而高效地处理任意长度的列表。
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
# 分别获取列表中每个元素并处理将包含大量重复的代码；每当名单的长度发生变化时，都必须修改代码。
# 使用 for 循环，可让 Python 去处理每个元素，从而避免这些问题。
# 定义一个 for 循环。这行代码让 Python 从列表 magicians 中取出一个名字，并将其与变量 magician 相关联。
# 最后，让 Python 打印前面赋给变量 magician 的名字。这样，对于列表中的每个名字，Python 都将重复执行最后两行代码。
# 循环很重要，因为它是让计算机自动完成重复工作的常见方式之一。

# for cat in cats:
# for dog in dogs:
# for item in list_of_items:
# 单数-复数写法更有可读性。

# 在 for 循环中，可以对每个元素执行任意操作。
# 相比于前一个示例，唯一的不同是为每位魔术师都打印一条以其名字为抬头的消息。
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# 在 for 循环中，想包含多少行代码都可以。
# 在代码行 for magicianin magicians 后面，每行缩进的代码都是循环的一部分，将针对列表中的每个值执行一次。
# 因此，可对列表中的每个值执行任意多的操作。在 for 循环后，可以包含任意多行代码。
# \n在每次循环结束插入一个空行。
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# for 循环结束后通常想提供总结性输出或接着执行程序必须完成的其他任务。
# 在 for 循环后面，没有缩进的代码都只执行一次，不会重复执行。
# 将相应的代码放在 for循环后面，且不缩进：
# 只执行一次。
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# Python 根据缩进来判断代码行与程序其他部分的关系。
# Python 通过缩进让代码更易读。简单地说，它要求你使用缩进让代码整洁且结构清晰。
# 在较长的 Python 程序中，将看到缩进程度各不相同的代码块，从而对程序的组织结构有大致的认识。
# 开始编写必须正确缩进的代码时，需要注意一些常见的缩进错误，下面将展示一些错误示例。

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)
# IndentationError: expected an indented block after 'for' statement on line 30
# 忘记缩进错误，位于 for 语句后面且属于循环组成部分的代码行，一定要缩进。
# 通常，将紧跟在 for 语句后面的代码行缩进，可消除这种缩进错误。

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
# Python 发现 for语句后面有一行代码是缩进的，因此没有报告错误。
# 但忘记缩进循环中的第二行代码行，这些Python语句是合法的，但没有达到预期的功能，存在逻辑错误。
# 有时候，虽然循环能够运行且不会出现错误，但结果出人意料。
# 当试图在循环中执行多项任务，却忘记缩进其中的一些代码行时，就会出现这种情况。

# message = "Hello Python world!"
#     print(message)
# 不必要的缩进，报错IndentationError: unexpected indent
# 不小心锁进了不需要缩进的代码，Python会报错。
# 为避免意外的缩进错误，请只缩进需要缩进的代码。

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you everyone, that was a great magic show!")
# 循环后不必要的缩进，也是逻辑错误。将原本应循环结束后执行一次的操作在循环内执行了多次。

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians
#   print(magician)
# for 语句末尾的冒号告诉 Python，下一行是循环的第一行。
# 遗漏了冒号，将导致语法错误。
# 报错，SyntaxError: expected ':'
# Python 不知道你只是忘记了冒号，还是想添加更多的代码来创建更复杂的循环。
# 如果解释器能够找出修复方案，它将提出建议，如在行尾添加冒号（这里它使用响应 expected ':' 指出了这一点）。
# 对于一些错误，Python 通过traceback 提供了修复建议，因此很容易修复。
# 但有些错误解决起来要困难得多，虽然最终的修复方案可能只是修改单个字符。

# 经常需要存储和处理一大组数。
# 列表非常适合用于存储数值集合，而 Python 提供了很多工具，可帮助你高效地处理数值列表。

# Python 函数 range() 让你能够轻松地生成一系列的数。
for value in range(1, 5):
    print(value)
# 打印1, 2, 3, 4
# 输出不包含第二个值
for value in range(1, 6):
    print(value)

# 在调用 range() 函数时，也可只指定一个参数，这样它将从 0 开始。
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
# range() 函数返回的不是一个列表（list），而是一个特殊的、不可变的range对象。
# 这个range对象，是一个可迭代对象（iterable）。
# range(1, 100)，如果是list，计算机会把100个都存储起来。
# 但对于range对象，计算机在内存中只存储了三个数字：起始值（默认为0）、结束值（10000）和步长（默认为1）。它并没有生成那10000个数字。
# 这个range对象非常懒惰和节约内存资源，只记录了生成数字的规则。
# 虽然它不是列表，但它的行为在很多方面和列表非常相似。
# 它是“可迭代的”（Iterable）：
# 这意味着您可以把它放在for循环里。当for循环向range对象要下一个数时，range对象会根据它内部的“公式”（起始值、结束值、步长）实时计算出下一个数并交出来，然后等待下一次的请求。
# 它支持常见的序列操作（而且效率很高）。
# len(range(0,100)) = 100，且时间复杂度为O(1)，只需100 - 0，不需要去数。
# 50 in range(0, 100)结果为True，时间复杂度O(1),数学判断不需要遍历元素。
# range(0, 100)[50]结果为50，复杂度为O(1)，因为是计算出来的。

# range() 在使用上像一个列表，但在实现上却是一个高效的、即时计算的数字序列生成器。
# 它用固定的、极小的内存空间，就能表示一个可能包含亿万个数字的序列，从而极大地节省了内存。

# range 是 Python 的一个内置不可变序列类型，其核心逻辑由 C 语言实现以获得高性能。
# 它的构造机制与 Python 的 *args 非常相似：它被设计用来接收一到三个整数作为位置参数。
# range 的内部逻辑会检查接收到的参数数量，并根据这个数量来决定哪个值是 start（起始值）、stop（结束值）和 step（步长）。
# 这是一种基于参数数量的、高度优化的规则系统，而非简单的函数默认值。
# stop 是不可省略的，如果只有一个参数，就是 stop 参数。如果有两个参数，就是 start 和 stop 参数。如果有三个参数，第三个就是 step 参数。

# 为了让代码更简洁，可不使用临时变量 square，而是直接将计算得到的每个值追加到列表末尾。
# 在创建更复杂的列表时，可使用上述两种方法中的任意一种。有时候，使用临时变量会让代码更易读；而在其他时候，这样做只会让代码无谓地变长。
# 首先应该考虑的是，编写清晰易懂且能完成所需功能的代码，等到审核代码时，再考虑采用更高效的方法。
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# 对数值列表执行简单的统计计算。
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表推导式(List Comprehensions)。
# 列表推导式将 for 循环和创建新元素的代码合并成一行，并自动追加新元素。
# 前面介绍的生成列表 squares 的方式包含三四行代码，而列表推导式只需编写一行代码就能生成这样的列表。
squares = [value**2 for value in range(1, 11)]
print(squares)
# 要使用这种语法，首先指定一个描述性的列表名，如 squares。然后指定一个左方括号，并定义一个表达式，用于生成要存储到列表中的值。
# 在这个示例中，表达式为 value**2，它计算平方值。
# 接下来，编写一个 for 循环，用于给表达式提供值，再加上右方括号。
# 在这个示例中，for 循环为 for value in range(1,11)，它将值 1～10 提供给表达式 value**2。请注意，这里的 for 语句末尾没有冒号。


# 切片用于处理列表的部分而不是全部元素
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
# 与range() 函数一样，Python 在到达指定的第二个索引之前的元素时停止。不包括第二个索引元素。
# 列表的切片也是一个列表。可以用切片生成列表的各种子集。
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:4])

# 如果没有指定第一个索引，Python 将自动从列表开头开始。
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[:4])

# 省略终止索引，自动终止于列表末尾。可以获得从特定位置到列表末尾的子列表。
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[2:])

# 索引也可以是负数，代表倒数第几个，可以输出列表末尾的任意切片。
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:-1])  # 从第一个开始，不包括倒数第一个。

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[-2:-1])
# 从倒数第二个开始，不包括倒数第一个 倒数第二个结束，输出只有一个元素的列表。

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[3:2])
# 输出空列表。

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[-3:])
# 无论列表怎么变化 输出最后三个元素。

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[::2])
# 可在表示切片的方括号内指定第三个值。这个值告诉 Python在指定范围内每隔多少元素提取一个。
# 从开头到结尾，两个元素一个。
# [start:stop]：使用一个冒号时，在处理 start 和 stop 这两个参数，而 step 参数会使用其默认值 1。
# 两个冒号，启用了第三个参数步长。

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
# a[::-1]: 这是最常用的反转写法。start 默认为最后一个元素，stop 默认为开头之前，step 为 -1。完整含义就是：最后一个元素开始，一个一个地向前取，直到取完所有元素为止。
# 切片操作会从 start 索引开始，以 step 为步长，提取元素，直到 stop 索引之前停止。stop 索引本身永远不会被包含在结果中。
# 情况一：step 为正数（或省略，默认为 +1）。
# 此时，切片方向为从左到右。
# start 省略时：默认值为 0，即从列表的第一个元素开始。
# stop 省略时：默认值为列表的长度 len(a)，即切片会一直持续到并包含列表的最后一个元素。
# 情况二：step 为负数。
# 此时，切片方向为从右向左。
# start 省略时：默认值为 -1 (或 len(a) - 1)，即从列表的最后一个元素开始。
# stop 省略时：默认值为列表的开头之前的位置。为了能包含索引为 0 的第一个元素，切片必须在它“左边”的位置停止。
# 如果没有提取到任何元素，返回空列表。


# 如果要遍历列表的部分元素，可在 for 循环中使用切片，实现对切片的遍历。
players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 在很多情况下，切片是很有用的。例如，在编写游戏时，可以在玩家退出游戏时将其最终得分加入一个列表。
# 然后将该列表按降序排列，再创建一个只包含前三个得分的切片，以获取该玩家的三个最高得分。
# 在处理数据时，可以使用切片来进行批量处理。
# 在编写 Web 应用程序时，可以使用切片来分页显示信息，并在每页上显示数量合适的信息。


# 列表复制，根据已有列表创建新列表。
# 要复制列表，可以创建一个包含整个列表的切片。
# 方法是同时省略起始索引和终止索引([:])。
# 与 list.copy() 一样，都生成原始列表的浅拷贝。
# 会在内存中创建一个全新的列表对象，但这个新列表中的元素是原始列表中元素的引用。
# 对于不可变元素（如数字、字符串、元组）：这没有实际影响，因为你不能原地修改它们。
# 对于可变元素（如嵌套的列表、字典）：这意味着如果你修改了原始列表中嵌套的那个可变元素，这个改动会同时反映在拷贝出来的新列表中，反之亦然。
# .copy() 是一个方法，只有实现了这个方法的对象才能调用（例如 list, dict, set）。
# [:] 是一种语法，适用于所有支持切片操作的序列类型（例如 list, tuple, str）。
# copy() 意图更明显，可读性更好。
# 要实现深拷贝（Deep Copy），需要使用 Python 标准库中的 copy 模块，具体来说，是 copy.deepcopy() 函数。
# 与浅拷贝不同，深拷贝会递归地复制所有嵌套的对象，创建一个完全独立、与原始对象没有任何关联的副本。
# 实现步骤非常简单：导入 copy 模块。调用 copy.deepcopy() 函数，并传入你想要拷贝的对象。


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
# 切片产生了两个list，创建了副本。


my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)
# 输出表明确实有两个列表，两个列表分别只添加了一个元素。

print("\nMy friend's favorite foods are:")
print(friend_foods)
# 这里将 my_foods 赋给 friend_foods，而不是将 my_foods 的副本赋给 friend_foods。
# 这种语法实际上是让 Python 将新变量friend_foods 关联到已与 my_foods 相关联的列表，因此这两个变量指向同一个列表。
# 有鉴于此，当我们将 'cannoli' 添加到 my_foods 中时，它也将出现在 friend_foods 中。
# 同样，虽然 'ice cream' 好像只被加入了friend_foods，但它也将同时出现在这两个列表中。
# 输出表明，这两个列表是相同的，这并非我们想要的结果。
