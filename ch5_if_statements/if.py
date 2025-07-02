cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# 每条 if 语句的核心都是一个值为 True 或 False 的表达式，这种表达式称为条件测试。
# Python 根据条件测试的值是 True 还是 False 来决定是否执行 if 语句中的代码。
# 如果条件测试的值为 True，Python 就执行紧跟在if 语句后面的代码；如果为 False，Python 就忽略这些代码。

car = "bmw"
print(car == "bmw")
car = "audi"
print(car == "bmw")
# 相等运算符==在它两边的值相等时返回 True，否则返回


car = "Audi"
print(car == "audi")
# 在 Python 中检查是否相等时是区分大小写的。、
# ，网站可能使用类似的条件测试来确保用户名是独一无二的，而并非只是与另一个用户名的大小写不同：
# 在用户提交新的用户名时，把它转换为全小写的，并与所有既有用户名的小写版本进行比较。


car = "Audi"
print(car.lower() == "audi")
print(car)
# 如果大小写无关紧要，lower也不会改变变量的值。


requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")
# 要判断两个值是否不等，可使用不等运算符（!=）
# 有时检查两个量是否不等效率更高

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age >= 21)
print(age > 21)

# 你可能想同时检查多个条件。使用and/or
# 比较运算符（如 >、<、>=、<=、==、!=）的优先级高于逻辑运算符（and、or、not）
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print((age_0 >= 21) and (age_1 >= 21))
# 括号改善可读性，但不是一定要这么写


# 关键字 or 也能够让你检查多个条件，但只要满足其中一个条件，就能通过整个条件测试。
# 仅当所有条件测试都没有通过时，使用 or 的表达式才为 False
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# 有时候，执行操作前必须检查列表是否包含特定的值。
# 要判断特定的值是否在列表中，可使用关键字 in。
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)
print("pepperoni" in requested_toppings)


# 还有些时候，确定特定的值不在列表中很重要。在这种情况下，可使用关键字 not
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# 你将遇到术语布尔表达式，它不过是条件测试的别名罢了。与条件表达式一样，
# 布尔表达式的结果要么为 True，要么为 False。
# if下，条件测试，条件表达式和布尔表达式是等价的。指if后面那个会得出True或False结果的表达式
game_active = True
can_edit = False
# 在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式


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

# 你经常需要在条件测试通过时执行一个操作，在没有通过时执行另一个操作。
# 在这种情况下，可使用 Python 提供的 if-else 语句。if-else 语句块类似于简单的 if 语句，
# 但其中的 else 语句让你能够指定条件测试未通过时要执行的操作。

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
# if-else 结构非常适合用于让 Python 执行两种操作之一的情形。
# 在这样简单的 if-else 结构中，总会执行两个操作中的一个。


# 你经常需要检查两个以上的情形，此时可使用 Python 提供的 if-elifelse 语句。
# Python 只执行 if-elif-else 结构中的一个代码块。它依次检查每个条件测试，直到遇到通过了的条件测试。
# 条件测试通过后，Python 将执行紧跟在它后面的代码，并跳过余下的条件测试
# elif 代码行其实是另一个 if 测试，它仅在前面的测试未通过时才会运行。
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
# 代码更简洁


# 可以使用任意数量的elif模块
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

# Python 并不要求 if-elif 结构后面必须有 else 代码块。在一些情况下，else 代码块很有用；
# 而在其他情况下，使用一条 elif 语句来处理特定的情形更清晰：

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
# 比上面使用else更清晰，经过这样的修改，每个代码块都仅在通过了相应的条件测试时才会执行
# else 是一条包罗万象的语句，只要不满足任何 if 或 elif 中的条件测试，其中的代码就会执行。
# 这可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个 elif 代码块来代替 else 代码块。
# 这样就可以肯定，仅当满足相应的条件时，代码才会执行。


# 在遇到通过了的条件测试后，Python 就会跳过余下的条件测试。这种行为很好，效率很高，让你能够测试一个特定的条件。
# 然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含 elif 和 else 代码块的简单 if 语句。
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

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
elif "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
elif "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
# 这样写代码不正确运行，只要通过了某个条件，就会跳过后面的判断
# 只运行一个代码块，就写if-elif-

# 结合使用 if 语句和列表，可完成一些有趣的任务：对列表中特定的值做特殊处理；
# 高效管理不断变化的情形，如餐馆是否还有特定的食材；证明代码在各种情形下都将按预期运行

# 检查特殊元素
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
# 假定青椒用完了，如果点了青椒，就指出不能点青椒的原因。else保证其他配料被添加


# 在运行 for 循环前确定列表非空很重要。
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
# 在 if 语句中将列表名用作条件表达式时，Python 将在列表至少包含一个元素时返回 True，在列表为空时返回 False
# 对于数值 0、空值 None、单引号空字符串 ''、双引号空字符串 ""、空列表 []、空元组 ()、空字典 {}，Python 都会返回 False。


available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
# 如果供应固定，也可用元组存储
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
# 使用多个列表模拟顾客要求配料没有的真实情景

# PEP 8 提供的唯一建议是：在诸如 ==、>= 和 <= 等比较运算符两边各添加一个空格。
