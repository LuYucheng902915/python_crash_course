# 在本章中，将学习编写函数（function）。
# 函数是带名字的代码块，用于完成具体的工作。要执行函数定义的特定任务，可调用（call）该函数。
# 当需要在程序中多次执行同一项任务时，无须反复编写完成该任务的代码，只需要调用执行该任务的函数，让 Python 运行其中的代码即可。
# 使用函数，程序编写、阅读、测试和修复起来都会更容易。
# 还将学习各种向函数传递信息的方式，学习编写主要任务是显示信息的函数，以及用于处理数据并返回一个或一组值的函数。
# 最后，将学习如何将函数存储在称为模块（module）的独立文件中，让主程序文件更加整洁。

from typing import Any

# 定义函数。


def greet_user():
    """显示简单的问候语"""
    print("Hello!")


greet_user()
print(greet_user.__doc__)
# 这个示例演示了最简单的函数结构。第一行代码使用关键字 def 来告诉Python，你要定义一个函数。
# 这是函数定义，向 Python 指出了函数名，还可以在括号内指出函数为完成任务需要什么样的信息。
# 在这里，函数名为不需要任何信息就能完成工作，因此括号内是空的（即便如此，括号也必不可少）。
# 最后，定义以冒号结尾。

# 紧跟在 def greet_user(): 后面的所有缩进行构成了函数体。
# 第二行的文本是称为文档字符串（docstring）的注释，描述了函数是做什么的。
# Python 在为程序中的函数生成文档时，会查找紧跟在函数定义后的字符串。
# 这些字符串通常前后分别用三个双引号引起，能够包含多行。

# 代码行 print("Hello!") 是函数体内的唯一一行代码，因此greet_user() 只做一项工作：打印 Hello!
# 要使用函数，必须调用它。函数调用让 Python 执行函数中的代码。要调用函数，可依次指定函数名以及用括号括起的必要信息。
# 由于这个函数不需要任何信息，调用它时括号内是空的即可。


# 向函数传递信息只需稍作修改，就可让函数在问候用户时以其名字作为抬头。
# 为此，可在函数定义 def greet_user() 的括号内添加username。
# 这样，可让函数接受你给 username 指定的任何值。现在，这个函数要求你在调用它时给 username 指定一个值。
# 因此在调用greet_user()，可将一个名字传递给它。
def greet_user1(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")


greet_user1("jesse")
# 代码 greet_user('jesse') 调用函数 greet_user()，并向它提供执行函数调用 print() 所需的信息。
# 这个函数接受你传递给它的名字，并向这个人发出问候。
# 可以根据需要调用函数greet_user() 任意多次，无论在调用时传入什么名字，都将生成相应的输出。
# 前面在定义 greet_user() 函数时，要求给变量 username 指定一个值。
# 这样，在调用这个函数并提供这种信息（人名）时，它将打印相应的问候语。

# 在 greet_user() 函数的定义中，变量 username 是一个形参（parameter），即函数完成工作所需的信息。
# 在代码greet_user('jesse') 中，值 'jesse' 是一个实参（argument），即在调用函数时传递给函数的信息。
# 在调用函数时，我们将要让函数使用的信息放在括号内。
# 在 greet_user('jesse') 这个示例中，我们将实参 'jesse'传递给函数 greet_user()，这个值被赋给了形参 username。
# 注意：大家有时候会形参、实参不分。即使你看到有人将函数定义中的变量称为实参或将函数调用中的变量称为形参，也不要大惊小怪。


# 函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
# 向函数传递实参的方式很多：既可以使用位置实参，这要求实参的顺序与形参的顺序相同。
# 也可以使用关键字实参，其中每个实参都由变量名和值组成。
# 还可以使用列表和字典。


# 在调用函数时，Python 必须将函数调用中的每个实参关联到函数定义中的一个形参。
# 最简单的方式是基于实参的顺序进行关联。以这种方式关联的实参称为位置实参。
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "harry")
# 这个函数的定义表明，它需要一个动物类型和一个名字。
# 在调用describe_pet() 时，需要按顺序提供一个动物类型和一个名字。按顺序将实参赋给形参。


# 可根据需要调用函数任意多次。要再描述一个宠物，只需再次调用describe_pet() 即可。
def describe_pet1(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet1("hamster", "harry")
describe_pet1("dog", "willie")
# 多次调用同一个函数是一种效率极高的工作方式。
# 只需在函数中编写一次描述宠物的代码，每当需要描述新宠物时，就都可以调用这个函数并向它提供新宠物的信息。
# 即便描述宠物的代码增加到了 10 行，依然只需使用一行调用函数的代码，就可以描述一个新宠物。
# 在函数中，可根据需要使用任意数量的位置实参，Python 将按顺序将函数调用中的实参关联到函数定义中相应的形参。


# 当使用位置实参来调用函数时，如果实参的顺序不正确，结果可能会出乎意料。
# 在这个函数调用中，先指定名字，再指定动物类型。得到了错误的结果。
def describe_pet2(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet2("harry", "hamster")


# 关键字实参是传递给函数的名值对。
# 这样会直接在实参中将名称和值关联起来，因此向函数传递实参时就不会混淆了。
# 关键字实参不仅让你无须考虑函数调用中的实参顺序，而且清楚地指出了函数调用中各个值的用途。
# 使用关键字实参调用。
def describe_pet3(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet3(animal_type="hamster", pet_name="harry")
describe_pet3(pet_name="harry", animal_type="hamster")
# 这次调用这个函数时，向Python 明确地指出了各个实参对应的形参。
# 关键字实参的顺序无关紧要。
# 注意：在使用关键字实参时，务必准确地指定函数定义中的形参名。
# 上面两个调用等价。


# 在编写函数时，可以给每个形参指定默认值。
# 如果在调用函数中给形参提供了实参，Python 将使用指定的实参值；否则，将使用形参的默认值。
# 给形参指定默认值后，可在函数调用中省略相应的实参。
# 使用默认值不仅能简化函数调用，还能清楚地指出函数的典型用法。
def describe_pet4(pet_name, animal_type="dog"):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet4("willie")
describe_pet4(pet_name="willie")
# 如果调用函数时描述的大多是小狗。
# 这里修改了 describe_pet() 函数的定义，在其中给形参animal_type 指定了默认值 'dog'。
# 这样，在调用这个函数时，如果没有给 animal_type 指定值，Python 将自动把这个形参设置为 'dog'。
# 在这个函数的定义中，修改了形参的排列顺序。
# 由于给animal_type 指定了默认值，无须通过实参来指定动物类型，因此函数调用只包含一个实参——宠物的名字。
# 然而，Python 依然将这个实参视为位置实参，如果函数调用只包含宠物的名字，这个实参将被关联到函数定义中的第一个形参。
# 这就是需要将 pet_name 放在形参列表开头的原因。
# 使用这个函数的最简单方式是，在函数调用中只提供小狗的名字。
# 只提供了一个实参 'willie'，这个实参将被关联到函数定义中的第一个形参 pet_name。
# 由于没有给animal_type 提供实参，因此 Python 使用默认值 'dog'。
describe_pet4(pet_name="harry", animal_type="hamster")
# 如果要描述的动物不是小狗，可使用类似于上面的函数调用：
# 由于显式地给 animal_type 提供了实参，Python 将忽略这个形参的默认值。


# 鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。
# def describe_pet4(pet_name, animal_type="dog"):
# 基于这种定义，在调用函数时，在任何情况下都必须给 pet_name 提供实参。
# 在指定该实参时，既可以使用位置实参，也可以使用关键字实参。
# 如果要描述的动物不是小狗，还必须在函数调用中给 animal_type 提供实参。
# 同样，在指定该实参时，既可以使用位置实参，也可以使用关键字实参。
# 下面的函数调用都是可行的。
# 一条名为 Willie 的小狗。
describe_pet4("willie")
describe_pet4(pet_name="willie")
# 一只名为 Harry 的仓鼠。
describe_pet4("harry", "hamster")
describe_pet4(pet_name="harry", animal_type="hamster")
describe_pet4(animal_type="hamster", pet_name="harry")
# 使用哪种调用方式无关紧要。只要函数调用能生成你期望的输出就好。


# 开始使用函数后，也许会遇到实参不匹配错误。
# 当提供的实参多于或少于函数完成工作所需的实参数量时，将出现实参不匹配错误。
def describe_pet5(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet5()
# TypeError: describe_pet5() missing 2 required positional arguments: 'animal_type' and 'pet_name'
# Python 发现该函数调用缺少必要的信息，并用 traceback 指出了这一点。
# traceback 首先指出问题出在什么地方，能够回过头去找出函数调用中的错误。
# 然后，指出导致问题的函数调用。最后，traceback 指出该函数调用缺少两个实参，并指出了相应形参的名称。
# 如果这个函数存储在一个独立的文件中，我们也许无须打开这个文件并查看函数的代码，就能重新正确地编写函数调用。


# Python 在参数匹配的时候，为了保证无歧义将传入实参匹配到函数定义的形参，通常遵循一些重要规则。
# 在函数调用时：位置实参必须在关键字实参之前。
# 函数定义时，带默认值的形参必须在没有默认值的形参之后。
# 在函数定义时：使用 / 可以强制其之前的参数只能按位置传递。
# 在函数定义时：使用 * 可以强制其之后的参数只能按关键字传递。
# 唯一性规则：在一次函数调用中，同一个参数不能被赋值多次。
# 可变参数规则 (*args 和 **kwargs) 。
# 描述：这是用来定义能接收任意数量实参的函数。它们分为两种，且必须按特定顺序出现：
# *args (可变位置参数): 它会收集所有未被其他形参捕获的多余位置实参，并打包成一个元组 (tuple)。
# 它必须在所有普通参数和关键字限定符 * 之后。
# **kwargs (可变关键字参数): 它会收集所有未被其他形参捕获的多余关键字实参，并打包成一个字典 (dict)。
# 它必须是函数定义中的最后一个参数。

# from typing import Any


# 定义一个包含所有参数类型的函数。
def process_data(
    source: str,
    destination: str,
    /,  # --- 1. 位置限定参数分隔符 ---
    mode: str = "fast",
    *filters: str,  # --- 2. 可变位置参数 ---
    force_overwrite: bool,
    timeout: int = 60,
    # *,  # --- 3. 关键字限定参数分隔符 (在这里是隐式的，因为 *filters 已经起到了作用) ---
    # 当函数不需要接收可变数量的位置参数（即没有 *args）时，就用一个单独的 * 来隔开。
    # 当函数需要接收可变数量的位置参数时，*args 本身就充当了分隔符，其后的所有参数都自动成为关键字限定。
    **metadata: Any,  # --- 4. 可变关键字参数 ---
):
    """
    一个演示所有Python参数类型的函数

    - `source`, `destination`: 只能按位置提供
    - `mode`: 可按位置或关键字提供
    - `*filters`: 接收任意数量的额外位置参数
    - `force_overwrite`, `timeout`: 必须按关键字提供（因为它们在 *filters 之后）
    - `**metadata`: 接收任意数量的额外关键字参数
    """
    print("--- 开始处理数据 ---")

    # 打印收到的所有参数的值和类型，以便观察
    print(f"  - source (位置限定): {source}")
    print(f"  - destination (位置限定): {destination}")
    print(f"  - mode (标准参数): {mode}")
    print(f"  - filters (可变位置, *args): {filters} (类型: {type(filters)})")
    print(f"  - force_overwrite (关键字限定): {force_overwrite}")
    print(f"  - timeout (关键字限定): {timeout}")
    print(f"  - metadata (可变关键字, **kwargs): {metadata} (类型: {type(metadata)})")

    print("--- 数据处理完成 ---\n")


process_data(
    # --- 阶段一：位置实参 ---
    # 这两个是必需的位置限定参数
    "/var/data/source.dat",
    "/var/output/report.csv",
    # 这是标准参数，按位置传递，覆盖了默认值 'fast'
    "full_analysis",
    # 这三个是多余的位置实参，将被 *filters 捕获
    "ignore_comments",
    "normalize_text",
    "deduplicate",
    # --- 阶段二：关键字实参 ---
    # 这是必需的关键字限定参数
    force_overwrite=True,
    # 这是可选的关键字限定参数，覆盖了默认值 60
    timeout=300,
    # 这两个是多余的关键字实参，将被 **metadata 捕获
    run_id="job-12345",
    executed_by="admin_user",
)

# 在一次函数调用中，你传递的实参（Arguments）只有两种类型，它们之间由逗号 , 分隔：
# 第一种是位置实参 (Positional Argument)。
# 它的“身份”就是一个单独的值或对象。
# Python 会根据它在调用中出现的顺序（位置）来决定把它赋给哪个形参。
# 第二种是关键字实参 (Keyword Argument)。
# 它的“身份”是一个关键字=值的组合。
# 它的作用是明确地告诉 Python：“请把等号右边的这个值，赋给函数定义中名叫这个‘关键字’的形参”。
# 它与位置无关，只认名字。
# 在一次函数调用中，这两种身份的实参必须遵循一个严格的顺序：所有位置实参，必须出现在所有关键字实参之前。
# 一旦开始使用关键字实参，就不能再回头插入位置实参了。

# 当 Python 解释器处理一个混合调用的函数时，它会遵循一个清晰的、分阶段的流程：
# 第一阶段绑定位置形参。
# 解释器从左到右扫描调用中的所有位置实参，并将它们依次绑定到函数定义的形参上（从左到右）。
# 如果遇到了 *args 形参，所有多余的位置实参都会被收集到 args 元组中。如果没有多余的，args 就是一个空元组。
# 第二阶段解释器接着绑定所有的关键字实参。
# 对于每一个 keyword=value，它在形参列表中按名称查找 keyword。
# 如果找到匹配的形参，并且该形参在第一阶段还未被赋值，就将 value 绑定给它。
# 如果遇到了 **kwargs 形参，所有多余的（即在形参列表中找不到对应名称的）关键字实参都会被收集到 kwargs 字典中。
# 第三阶段，应用默认值与最终检查
# 在以上两个阶段结束后，解释器检查所有形参。
# 对于任何仍未被赋值且带有默认值的形参，将其默认值绑定给它。
# 最后进行最终检查：如果此时仍有任何不带默认值的形参没有被赋值，Python 就会立即报错 TypeError: missing required positional argument

# 常见错误：
# TypeError: func() got multiple values for argument '...'
# 最常见的原因是，一个参数先通过位置被赋值，之后又试图通过关键字再次为它赋值。
# TypeError: func() missing X required positional argument(s): '...'
# 错误原因：调用函数时，未能提供足够的值给那些没有默认值的必需参数。
# TypeError: func() takes X positional arguments but Y were given
# 传入的位置实参数量，超过了函数定义能接收的数量上限，并且函数没有 *args 来“接住”这些多余的参数。
# TypeError: func() got an unexpected keyword argument '...'
# 传入了一个函数定义中不存在的关键字参数，并且函数没有 **kwargs 来收集这些未知的关键字参数。
# TypeError: func() missing X required keyword-only argument(s): '...'
# 未能通过关键字提供一个在 * 或 *args 之后定义的、且没有默认值的必需参数。
# TypeError: func() takes no arguments
# 调用了一个定义为不接收任何参数的函数，却在调用时给它提供了参数。


# 函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值。
# 函数返回的值称为返回值。在函数中，可以使用 return 语句将值返回到调用函数的那行代码。
# 返回值让你能够将程序的大部分繁重工作移到函数中完成，从而简化主程序。


# 下面来看一个函数，它接受名和姓并返回标准格式的姓名：
def get_formatted_name(first_name, last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
# 在调用可以返回值的函数时，需要提供一个变量，以便将返回的值赋给它。


# 有时候，需要让实参变成可选的，以便使用函数的人只在必要时才提供额外的信息。
# 可以使用默认值来让实参变成可选的。
# 假设要扩展 get_formatted_name() 函数，使其除了名和姓之外还可以处理中间名。
def get_formatted_name1(first_name, middle_name, last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name1("john", "lee", "hooker")
print(musician)


# 然而，并非所有人都有中间名。如果调用这个函数时只提供了名和姓，它将不能正确地运行。
# 为让中间名变成可选的，可给形参 middle_name 指定默认值（空字符串），在用户不提供中间名时不使用这个形参。
# 为了让get_formatted_name() 在没有提供中间名时依然正确运行，可给形参middle_name 指定默认值（空字符串），并将其移到形参列表的末尾：
def get_formatted_name2(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name2("jimi", "hendrix")
print(musician)
musician = get_formatted_name2("john", "hooker", "lee")
print(musician)
# 中间名是可选的，因此在函数定义中最后列出该形参，并将其默认值设置为空字符串。
# Python 将非空字符串解读为True，如果在函数调用中提供了中间名，条件测试 if middle_name 将为True。
# 在函数调用行，将返回的值赋值给变量并打印。
# 在调用这个函数时，如果只想指定名和姓，调用起来将非常简单。
# 如果还要指定中间名，就必须确保它是最后一个实参，这样 Python 才能正确地将位置实参关联到形参。
# 可选值在让函数能够处理各种不同情形的同时，确保函数调用尽可能简单。


# 函数可返回任何类型的值，包括列表和字典等较为复杂的数据结构。
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician)
# 函数将接受的文本信息放在一个更合适的数据结构中。使得后续可以以其他形式处理。


def build_person1(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person1("jimi", "hendrix", age=27)
print(musician)
# 在函数定义中，新增了一个可选形参 age，其默认值被设置为特殊值None（表示变量没有值）。
# 可将 None 视为占位值。在条件测试中，None 相当于 False。
# 如果函数调用中包含形参 age 的值，这个值将被存储到字典中。
# 在任何情况下，这个函数都会存储一个人的姓名，并且可以修改它，使其同时存储有关这个人的其他信息。


# 结合使用函数和 while循环,可将函数与本书前面介绍的所有 Python 结构结合起来使用。
def get_formatted_name3(first_name, last_name):
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name3(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
# 要让用户能够尽可能容易地退出，因此在每次提示用户输入时，都应提供退出途径。
# 使用 break 语句可以在每次提示用户输入时提供退出循环的简单途径。
# 在每次提示用户输入时，都检查他输入的是否是退出值。
# 如果是，就退出循环。现在，这个程序将不断地发出问候，直到用户输入的姓或名为 'q'。


# 向函数传递列表很有用，可能是名字列表、数值列表或更复杂的对象列表（如字典）。
# 将列表传递给函数后，函数就能直接访问其内容。下面使用函数来提高处理列表的效率。
def greet_users(names):
    """向列表中的每个用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)
# 向列表中的每个用户发出问候，将名字列表传递给函数。
# 函数接受一个列表，这个函数遍历接收到的列表，并对其中每个用户打印一条问候语。
# 在函数外，先定义一个用户列表 usernames，再调用 greet_users() 并将这个列表传递给它。
# 每当需要问候一组用户，可以调用这个函数。

# 将列表传递给函数后，函数就可以对其进行修改了。在函数中对这个列表所做的任何修改都是永久的。

# 需要打印的设计事先存储在一个列表中，打印后将被移到另一个列表中。
# 下面是在不使用函数的情况下模拟这个过程的代码。
# 首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止。
# 打印每个设计后，都将其移到列表 completed_models 中。
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型。
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# 重新组织代码，编写两个函数，每个函数做一件具体工作。
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models 中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """
    显示打印好的所有模型
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# 定义函数 print_models()，它包含两个形参：一个需要打印的设计列表和一个打印好的模型列表。
# 给定这两个列表，这个函数模拟打印每个设计的过程：将设计逐个从未打印的设计列表中取出，并加入打印好的模型列表。
# 然后，定义函数 show_completed_models()，它包含一个形参：打印好的模型列表。
# 给定这个列表，函数show_completed_models() 显示打印出来的每个模型的名称。

# 虽然这个程序的输出与未使用函数的版本相同，但是代码更有条理。
# 完成大部分工作的代码被移到了两个函数中，让主程序很容易理解。
# 只要看看主程序，你就能轻松地知道这个程序的功能。
# 描述性的函数名让阅读这些代码的人也能一目了然，虽然其中没有任何注释。

# 创建了一个未打印的设计列表，以及一个空列表，后者用于存储打印好的模型。
# 接下来，由于已经定义了两个函数，因此只需要调用它们并传入正确的实参即可。
# 调用 print_models() 并向它传递两个列表。像预期的一样，print_models() 模拟了打印设计的过程。
# 接下来，调用show_completed_models()，并将打印好的模型列表传递给它，让它能够指出打印了哪些模型。
# 描述性的函数名让阅读这些代码的人也能一目了然，虽然其中没有任何注释。

# 相比于没有使用函数的版本，这个程序更容易扩展和维护。
# 如果以后需要打印其他设计，只需再次调用 print_models() 即可。
# 如果发现需要对模拟打印的代码进行修改，只需修改这些代码一次，就将影响所有调用该函数的地方。
# 与必须分别修改程序的多个地方相比，这种修改的效率更高。

# 这个程序还演示了一种理念：每个函数都应只负责一项具体工作。
# 用第一个函数打印每个设计，用第二个函数显示打印好的模型，优于使用一个函数完成这两项工作。
# 在编写函数时，如果发现它执行的任务太多，请尝试将这些代码划分到两个函数中。
# 别忘了，总是可以在一个函数中调用另一个函数，这有助于将复杂的任务分解成一系列步骤。


# 有时候，需要禁止函数修改列表。
# 假设像前一个示例那样，你有一个未打印的设计列表，并且编写了一个将这些设计移到打印好的模型列表中的函数。
# 可能会做出这样的决定：即便打印了所有的设计，也要保留原来的未打印的设计列表，作为存档。
# 但由于将所有的设计都移出了unprinted_designs，这个列表变成了空的——原来的列表没有了。
# 为了解决这个问题，可向函数传递列表的副本而不是原始列表。
# 这样，函数所做的任何修改都只影响副本，而丝毫不影响原始列表。
print_models(unprinted_designs[:], completed_models)
# 用切片表示法创建列表的副本。
# 上面的调用不会清空未打印的设计列表。
# print_models() 函数依然能够完成其工作，因为它获得了所有未打印的设计的名称，但它这次使用的是列表 unprinted_designs 的副本，而不是列表 unprinted_designs 本身。
# 函数所做的修改不会影响列表 unprinted_designs。
# 向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由，否则还是应该将原始列表传递给函数。
# 这是因为，让函数使用现成的列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此。


# 可以传递任意数量实参，有时候预先不知道函数需要接受多少个实参，好在 Python 允许函数从调用语句中收集任意数量的实参。
# 例如一个制作比萨的函数，它需要接受很多配料，但无法预先确定顾客要点多少种配料。
# 下面的函数只有一个形参 *
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")
# 形参名 *toppings 中的星号让 Python 创建一个名为 toppings 的元组，该元组包含函数收到的所有值。
# 函数体内的函数调用 print() 生成的输出证明，Python 既能处理使用一个值调用函数的情形，也能处理使用三个值调用函数的情形。
# 它以类似的方式处理不同的调用。注意，Python 会将实参封装到一个元组中，即便函数只收到一个值也是如此。
# 不管函数收到多少实参，语法都管用。


# 可以将函数调用 print() 替换为一个循环，遍历配料列表并对顾客点的比萨进行描述：
def make_pizza1(*toppings):
    """
    概述要制作的比萨
    """
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza1("pepperoni")
make_pizza1("mushrooms", "green peppers", "extra cheese")


# 结合使用位置实参和任意数量的实参。
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python 先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
# 不够严谨，上面已经阐述了严格的函数定义中形参的定义。
# 如果前面的函数还需要一个表示比萨尺寸的形参，必须将该形参放在形参 *toppings 的前面。
def make_pizza2(size, *toppings):
    """概述要制作的比萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza2(16, "pepperoni")
make_pizza2(12, "mushrooms", "green peppers", "extra cheese")
# 基于上述函数定义，Python 将收到的第一个值赋给形参 size，将其他所有的值都存储在元组 toppings 中。
# 在函数调用中，首先指定表示比萨尺寸的实参，再根据需要指定任意数量的配料。
# 经常会看到通用形参名 *args，它也这样收集任意数量的位置实参。


# 有时候，要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
# 在这种情况下，可将函数编写成能够接受任意数量的键值对——调用语句提供了多少就接受多少。
# 一个这样的示例是创建用户简介：你知道将收到有关用户的信息，但不确定是什么样的信息。
# 在下面的示例中，build_profile() 函数不仅接受名和姓，还接受任意数量的关键字实参。
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)
# build_profile() 函数的定义要求提供名和姓，同时允许根据需要提供任意数量的名值对。
# 形参 **user_info 中的两个星号让 Python 创建一个名为 user_info 的字典，该字典包含函数收到的其他所有名值对。
# 在这个函数中，可以像访问其他字典那样访问 user_info 中的名值对。
# 在函数体内，将名和姓加入字典user_info，因为总是会从用户那里收到这两项信息，而这两项信息还没被放在字典中。接下来，将字典 user_info 返回函数调用行。
# 在调用这个函数时，不管额外提供多少个键值对，它都能正确地处理。
# 在编写函数时，可以用各种方式混合使用位置实参、关键字实参和任意数量的实参。
# 知道这些实参类型大有裨益，因为你在阅读别人编写的代码时经常会见到它们。
# 要正确地使用这些类型的实参并知道使用它们的时机，需要一定的练习。就目前而言，牢记使用最简单的方法来完成任务就好了。
# 继续往下阅读，你就会知道在各种情况下使用哪种方法的效率最高。
# 经常会看到形参名 **kwargs，它用于收集任意数量的关键字实参。
