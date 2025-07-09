# 编程时经常需要检查一系列条件，并据此决定采取什么措施。
# 在Python 中，if 语句让你能够检查程序的当前状态，并采取相应的措施。
# 在本章中，你将学习条件测试，以检查你感兴趣的任何条件。
# 你将学习简单的 if 语句，以及如何创建一系列复杂的 if 语句来确定当前到底处于什么条件下。
# 接下来，你将把学到的知识应用于列表：编写一个 for 循环，以一种方式处理列表中的大多数元素，以另一种方式处理包含特定值的元素。
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# 每条 if 语句的核心都是一个值为 True 或 False 的表达式，这种表达式称为条件测试。
# Python 根据条件测试的值是 True 还是 False 来决定是否执行 if 语句中的代码。
# 如果条件测试的值为 True，Python 就执行紧跟在if 语句后面的代码；如果为 False，Python 就忽略这些代码。

# 大多数条件测试将一个变量的当前值与特定的值进行比较。
# 最简单的条件测试检查变量的值是否与特定的值相等：
car = "bmw"
print(car == "bmw")
car = "audi"
print(car == "bmw")
# 相等运算符 == 在它两边的值相等时返回 True，否则返回False。


car = "Audi"
print(car == "audi")
# 在 Python 中检查是否相等时是区分大小写的。
# 如果大小写无关紧要，只想检查变量的值，可先将变量的值转换为全小写的，再进行比较。
# 网站可能使用类似的条件测试来确保用户名是独一无二的，而并非只是与另一个用户名的大小写不同。
# 在用户提交新的用户名时，把它转换为全小写的，并与所有既有用户名的小写版本进行比较。


car = "Audi"
print(car.lower() == "audi")
print(car)
# 无论值 'Audi' 的大小写如何，上述条件测试都将返回 True，因为它不区分大小写。
# lower() 方法不会修改存储在变量 car 中的值，因此进行这样的比较不会影响原来的变量。


requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")
# 要判断两个值是否不等，可使用不等运算符（!=）
# 如果两个值不等将返回 True，进而执行紧跟在 if 后的代码/
# 有时检查两个量是否不等效率更高。

# 数值比较。
age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# 条件语句可包含各种数学比较，如小于、小于等于、大于、大于等于。
# 每种数学比较都能成为 if 语句的一部分，从而让你能够直接检查你感兴趣的多个条件。
age = 19
print(age < 21)
print(age <= 21)
print(age >= 21)
print(age > 21)

# 你可能想同时检查多个条件。使用 and/or。
# 要检查两个条件是否都为 True，可使用关键字 and 将两个条件测试合而为一。
# 如果每个条件测试都通过了，整个表达式就为 True；如果至少一个条件测试没有通过，整个表达式就为 False。
# 比较运算符（如 >、<、>=、<=、==、!=）的优先级高于逻辑运算符（and、or、not）。
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print((age_0 >= 21) and (age_1 >= 21))
# 为了改善可读性，可将每个条件测试都分别放在一对括号内，但并非必须这样做。


# 关键字 or 也能够让你检查多个条件，但只要满足其中一个条件，就能通过整个条件测试。
# 仅当所有条件测试都没有通过时，使用 or 的表达式才为 False。
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)
# 逻辑运算遵循短路求值”（Short-circuit Evaluation）。
# 是指在逻辑运算（and 和 or）中，如果仅通过第一部分表达式的值就已经能确定整个表达式的最终结果，那么第二部分（以及后续部分）的表达式将不会被执行或求值。
# 对于 A and B：Python 从左到右计算表达式 A。
# 如果 A 的布尔值为 False，那么整个 A and B 表达式的结果必定为 False。
# 此时，Python 会立即“短路”，直接返回 A 的值，而完全不会去计算或执行 B。
# 只有当 A 的布尔值为 True 时，Python 才会接着计算 B，并返回 B 的值作为整个表达式的结果。
# 短路求值可以提高性能，还可以实现更安全和简洁的控制流。
# 它允许我们编写一种称为 “守护表达式”（Guard Clause） 的代码模式，可以有效避免运行时错误。
# 例如避免空指针或属性错误：在访问一个对象的属性或方法之前，先检查该对象是否为 None。
# if user is not None and user.is_active:
# 避免除以零的错误：在进行除法运算前，先检查除数是否为零。
# if divisor != 0 and value / divisor > 10:
# 检查列表/字典是否为空或包含某个键：
# if my_list and my_list[0] == 'a':
# if 'key' in my_dict and my_dict['key'] == 'valid':

# 有时候，执行操作前必须检查列表是否包含特定的值。
# 例如，在结束用户的注册过程之前，需要检查他提供的用户名是否已在用户名列表中；在地图程序中，需要检查用户提交的位置是否在已知位置的列表中。
# 要判断特定的值是否在列表中，可使用关键字 in。
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)
print("pepperoni" in requested_toppings)


# 还有些时候，确定特定的值不在列表中很重要。在这种情况下，可使用关键字 not in。
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# 随着对变成了解的深入，将遇到术语布尔表达式，它不过是条件测试的别名罢了。
# 与条件表达式一样，布尔表达式的结果要么为 True，要么为 False。
# if 下，条件测试，条件表达式和布尔表达式是等价的。指 if 后面那个会得出 True 或 False 结果的表达式。
game_active = True
can_edit = False
# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。

# 理解条件测试之后，就可以开始编写 if 语句了。
# if 语句有很多种，选择使用哪一种取决于要测试的条件数。
# 最简单的 if 语句只有一个条件测试和一个操作：
# if conditional_test: do something
# 第一行可包含任意条件测试，而在紧跟在测试后面的缩进代码块中，可执行任意操作。
# 如果条件测试的结果为 True，Python 就会执行紧跟在 if 语句后面的代码，否则 Python 将忽略这些代码。
age = 19
if age >= 18:
    print("You are old enough to vote!")

# 在 if 语句中，缩进的作用与 for 循环中相同。如果条件测试通过了，将执行 if 语句后面所有缩进的代码行，否则将忽略它们。
# 可根据需要，在紧跟在 if 语句后面的代码块中添加任意数量的代码行。
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# 经常需要在条件测试通过时执行一个操作，在没有通过时执行另一个操作。
# 在这种情况下，可使用 Python 提供的 if-else 语句。
# if-else 语句块类似于简单的 if 语句，但其中的 else 语句让你能够指定条件测试未通过时要执行的操作。

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# if-else 结构非常适合用于让 Python 执行两种操作之一的情形。
# 在这样简单的 if-else 结构中，总会执行两个操作中的一个。


# 你经常需要检查两个以上的情形，此时可使用 Python 提供的 if-elif-else 语句。
# Python 只执行 if-elif-else 结构中的一个代码块。它依次检查每个条件测试，直到遇到通过了的条件测试。
# 条件测试通过后，Python 将执行紧跟在它后面的代码，并跳过余下的条件测试。
# elif 代码行其实是另一个 if 测试，它仅在前面的测试未通过时才会运行。
# 如果 if 测试和 elif 测试都未通过，Python 将运行处 else 代码块中的代码。
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
# 代码更简洁。
# 像上一个示例那样，缩进的代码行根据年龄设置变量 price 的值。
# 在 if-elif-else 语句中设置 price 的值后，一个未缩进的函数调用 print() 会根据这个变量的值打印一条消息，指出门票价格。


# 可以根据需要使用任意数量的 elif 模块。
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

# Python 并不要求 if-elif 结构后面必须有 else 代码块。在一些情况下，else 代码块很有用；而在其他情况下，使用一条 elif 语句来处理特定的情形更清晰。
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
# 比上面使用 else 更清晰，经过这样的修改，每个代码块都仅在通过了相应的条件测试时才会执行。
# else 是一条包罗万象的语句，只要不满足任何 if 或 elif 中的条件测试，其中的代码就会执行。
# 这可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个 elif 代码块来代替 else 代码块。
# 这样就可以肯定，仅当满足相应的条件时，代码才会执行。

# if-elif-else 语句虽然功能强大，但仅适用于只有一个条件满足的情况。
# 在遇到通过了的条件测试后，Python 就会跳过余下的条件测试。这种行为很好，效率很高，让你能够测试一个特定的条件。
# 然而，有时候必须检查你关心的所有条件。
# 在这种情况下，应使用一系列不包含 elif 和 else 代码块的简单 if 语句。
# 在可能有多个条件为True，且需要在每个条件为 True 时都采取相应措施时，适合使用这种方法。
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
# 多个if 不管前面条件判断有没有通过，都会进行下面的条件判断。
# 每当这个程序运行时，都会执行这三个独立的条件测试。

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
elif "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
elif "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
# 这样写代码不能正确实现需要的逻辑，只要通过了某个条件，就会跳过后面的判断。
# 结果就是只能添加顾客点的第一种配料。
# 总之，如果只想运行一个代码块，就使用 if-elif-else 语句；如果要运行多个代码块，就使用一系列独立的 if 语句。


# 结合使用 if 语句和列表，可完成一些有趣的任务：对列表中特定的值做特殊处理；高效管理不断变化的情形；证明代码在各种情形下都将按预期运行。

# 检查列表中的特殊元素并进行合适的处理。
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
# 这里在为比萨添加每种配料前都进行检查。假定青椒用完了，如果点了青椒，就指出不能点青椒的原因。else保证其他配料被添加。

# 到目前为止，对于要处理的每个列表都做了一个简单的假设——它们都至少包含一个元素。
# 因为马上就要让用户来提供存储在列表中的信息，所以不能再假设循环运行时列表非空。
# 在运行 for 循环前确定列表非空很重要。
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# 首先创建一个空列表，然后进行简单的检查。
# 在 if 语句中将列表名用作条件表达式时，Python 将在列表至少包含一个元素时返回 True，在列表为空时返回 False
# 对于数值 0、空值 None、单引号空字符串 ''、双引号空字符串 ""、空列表 []、空元组 ()、空字典 {}，Python 都会返回 False。


# 如何制作比萨前拒绝怪异的配料要求。
# 下面的示例定义了两个列表，其中第一个包含比萨店供应的配料，第二个则包含顾客点的配料。
# 这次对于 requested_toppings 中的每个元素，都先检查它是否是比萨店供应的配料，再决定是否在比萨中添加它。
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
# 如果供应固定，也可用元组存储。
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
# 创建另一个列表，其中包含顾客点的配料。
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
# 使用多个列表模拟顾客要求配料没有的真实情景。


# 在条件测试的格式设置方面，PEP 8 提供的唯一建议是：在诸如 ==、>= 和 <= 等比较运算符两边各添加一个空格。
# 这样的空格不会影响 Python 对代码的解读，只是让代码阅读起来更容易。
