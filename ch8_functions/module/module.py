# 将函数存储在模块中使用函数的优点之一是可将代码块与主程序分离。
# 通过给函数指定描述性名称，能让程序容易理解得多。
# 还可以更进一步，将函数存储在称为模块的独立文件中，再将模块导入（import）主程序。
# import 语句可让你在当前运行的程序文件中使用模块中的代码。

# 通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。
# 这还能让你在众多不同的程序中复用函数。
# 将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。
# 知道如何导入函数还能让你使用其他程序员编写的函数库。

# 导入整个模块,要让函数是可导入的，得先创建模块。
# 模块是扩展名为 .py 的文件，包含要导入程序的代码。
# 下面来创建一个包含 make_pizza() 函数的模块。
# 在文件 pizza.py 中给出 make_pizza() 函数的定义和实现。
import pizza
import pizza as p
from pizza import make_pizza
from pizza import make_pizza as mp

pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
# 先导入模块，再调用 make_pizza() 两次。
# 当 Python 读取这个文件时，代码行 import pizza 会让 Python 打开文件 pizza.py，并将其中的所有函数都复制到这个程序中。
# 看不到复制代码的过程，因为 Python 会在程序即将运行时在幕后复制这些代码。
# 于是可以使用 pizza.py 中定义的所有函数。
# 要调用被导入模块中的函数，可指定被导入模块的名称 pizza 和函数名make_pizza()，并用句点隔开。
# 这就是一种导入方法：只需编写一条 import 语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。
# 如果使用这种 import 语句导入了名为 module_name.py 的整个模块，就可使用下面的语法来使用其中的任意一个函数：
# module_name.function_name()


# 还可以只导入模块中的特定函数，语法如下：
# from module_name import function_name
# 用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
# from module_name import function_0, function_1,

# from pizza import make_pizza
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")
# 使用这种语法，在调用函数时则无须使用句点。
# 由于在 import 语句中显式地导入了 make_pizza() 函数，因此在调用时只需指定其名称即可。


# 使用 as 给函数指定别名。
# 如果要导入的函数的名称太长或者可能与程序中既有的名称冲突，可指定简短而独一无二的别名（alias）：
# 函数的另一个名称，类似于外号。要给函数指定这种特殊的外号，需要在导入时这样做。
# 下面给 make_pizza() 函数指定了别名 mp()。
# 这是在 import 语句中使用 make_pizza as mp 实现的，关键字 as 将函数重命名为指定的别名：
# from pizza import make_pizza as mp

mp(16, "pepperoni")
mp(12, "mushrooms", "green peppers", "extra cheese")
# 上面的import 语句将函数 make_pizza() 重命名为 mp()。
# 在这个程序中，每当需要调用 make_pizza() 时，都可将其简写成 mp()。
# Python 将运行 make_pizza() 中的代码，同时避免与程序可能包含的make_pizza() 函数混淆。
# 假设在你当前写的这个项目文件（比如 main.py）里，你为了某个特殊功能，自己也创建了一个名叫 make_pizza() 的函数。
# 现在，你想从外部模块 pizza.py 导入另一个同名函数。
# 这个外部模块 pizza.py 里也有一个 make_pizza() 函数，但它的功能和你的不一样。
# 如果直接导入，就会产生“混淆”（名称冲突）。
# 使用 as 别名来解决混淆。
# 通过使用别名，你可以清晰地告诉 Python 每一个名字分别指向什么。

# 指定别名的通用语法如下：
# from module_name import function_name as fn

# 还可以给模块指定别名。通过给模块指定简短的别名（如给 pizza 模块指定别名 p），你能够更轻松地调用模块中的函数。
# import pizza as p

p.make_pizza(16, "pepperoni")
p.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
# 上述 import 语句给 pizza 模块指定了别名 p，但该模块中所有函数的名称都没变。
# 要调用 make_pizza() 函数，可将其写为 p.make_pizza()而不是 pizza.make_pizza()。
# 这样不仅让代码更加简洁，还让你不用再关注模块名，只专注于描述性的函数名。
# 这些函数名明确地指出了函数的功能，对于理解代码来说，它们比模块名更重要。
# 给模块指定别名的通用语法如下：
# import module_name as mn

# 使用星号（*）运算符可让 Python 导入模块中的所有函数：
# from pizza import *
# import 语句中的星号让 Python 将模块 pizza 中的每个函数都复制到这个程序文件中。
# 由于导入了每个函数，可通过名称来调用每个函数，无须使用点号（dot notation）。
# 在使用并非自己编写的大型模块时，最好不要使用这种导入方法，因为如果模块中有函数的名称与当前项目中既有的名称相同，可能导致意想不到的结果：
# Python 可能会因为遇到多个名称相同的函数或变量而覆盖函数，而不是分别导入所有的函数。

# 最佳的做法是，要么只导入需要使用的函数，要么导入整个模块并使用点号。这都能让代码更清晰，更容易阅读和理解。


# 函数编写指南：
# 在编写函数时，需要牢记几个细节。应给函数指定描述性名称，且只使用小写字母和下划线。
# 描述性名称可帮助你和别人明白代码想要做什么。在给模块命名时也应遵循上述约定。
# 每个函数都应包含简要阐述其功能的注释。
# 该注释应紧跟在函数定义后面，并采用文档字符串的格式。
# 这样，其他程序员只需阅读文档字符串中的描述就能够使用它：
# 他们完全可以相信代码会如描述的那样运行，并且只要知道函数名、需要的实参以及返回值的类型，就能在自己的程序中使用它。

# 在给形参指定默认值时，等号两边不要有空格：
# def function_name(parameter_0, parameter_1='default value')
# 函数调用中的关键字实参也应遵循这种约定：
# function_name(value_0, parameter_1='value')


# PEP 8 建议代码行的长度不要超过 79 个字符。这样，只要编辑器窗口适中，就能看到整行代码。
# 如果形参很多，导致函数定义的长度超过了 79 个字符，可在函数定义中输入左括号后按回车键，并在下一行连按两次制表符键，从而将形参列表和只缩进一层的函数体区分开来。
# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#    return 0
def function_name(
    parameter_0,
    parameter_1,
    parameter_2,
    parameter_3,
    parameter_4,
    parameter_5,
    parameter_6,
    parameter_7,
):
    return 0


# 上面是自动格式化工具调整的格式。

# 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开。这样将更容易知道前一个函数到什么地方结束，下一个函数从什么地方开始。
# 所有的 import 语句都应放在文件开头。唯一的例外是，你要在文件开头使用注释来描述整个程序。
