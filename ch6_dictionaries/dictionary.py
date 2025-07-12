# 将学习能够将相关信息关联起来的 Python 字典，以及如何访问和修改字典中的信息。
# 字典可存储的信息量几乎不受限制，因此我们会演示如何遍历字典中的数据。
# 另外，你还将学习如何存储字典的列表、列表的字典和字典的字典。
# 理解字典后，就能够更准确地为各种真实物体建模。
from typing import cast

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])
# 字典 alien_0 存储了这个外星人的颜色和分数。
# 最后两行代码访问并显示这些信息。字典能够高效模拟现实世界的情形。

# 在 Python 中，字典（dictionary）是一系列键值对。每个键都与一个值关联，
# 可以使用键来访问与之关联的值。与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任意 Python 对象用作字典中的值。
# 在 Python 中，字典用放在花括号 ({}) 中的一系列键值对表示。
# 键值对包含两个相互关联的值。当你指定键时，Python 将返回与之关联的值。键和值之间用冒号分隔，而键值对之间用逗号分隔。
# 最简单的字典只有一个键值对，存储了一项有关信息。可以有空字典。
alien_0 = {"color": "green"}


# 要获取与键关联的值，可指定字典名并把键放在后面的方括号内。
print(alien_0["color"])
# 字典可以包含任意数量的键值对。
alien_0 = {"color": "green", "points": 5}
new_points = alien_0["points"]
print(f"You just earned {new_points} points!")
# 通过上面代码获取玩家消灭外星人获得的分数。

# 字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典名、用方括号括起来的键和与该键关联的值。
# 下面来在字典 alien_0 中添加两项信息：外星人的 x 坐标和 y 坐标，以便在屏幕的特定位置上显示该外星人。
# 将这个外星人放在屏幕左边缘上，距离屏幕上边缘 25 像素。
# 由于屏幕坐标系的原点通常在左上角，因此要将该外星人放在屏幕左边缘，可将 x 坐标设置为 0；要将该外星人放在距离屏幕上边缘 25 像素的地方，可将 y 坐标设置为 25。
alien_0 = {"color": "green", "points": 5}
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
# 字典会保留定义时的元素排列顺序。如果将字典打印出来或遍历其元素，将发现元素的排列顺序与其添加顺序相同。

# 可先使用一对空花括号定义一个空字典，再分行添加各个键值对。
alien_0 = {}
alien_0 = dict()
# 调用不含参数的字典构造函数也返回空字典。
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)
# 如果要使用字典来存储用户提供的数据或者编写能自动生成大量键值对的代码，通常需要先定义一个空字典。


# 要修改字典中的值，可依次指定字典名、用方括号括起来的键和与该键关联的新值。
alien_0 = {"color": "green", "points": 5}
print(f"The alien is {alien_0['color']}.")
alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")

# 来看一个更有趣的例子：对一个能够以不同速度移动的外星人进行位置跟踪。
# 为此，存储该外星人的当前速度，并据此确定该外星人应该向右移动多远。
alien_0_new: dict[str, str | int] = {
    "x_position": 0,
    "y_position": 25,
    "speed": "medium",
}
print(f"Original position: {alien_0_new['x_position']}")
if alien_0_new["speed"] == "slow":
    x_increment = 1
elif alien_0_new["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
# 使用 cast 告诉 Mypy，我们确信这里的 "x_position" 是一个整数，为了静态类型检查。
# cast 不会对实际运行的代码产生任何影响，它只在类型检查阶段起作用。
current_x = cast(int, alien_0_new["x_position"])
# 现在 Mypy 就知道 current_x 是 int，可以安全地进行加法运算了。
alien_0_new["x_position"] = current_x + x_increment
# 原来类型检查报错的代码： alien_0_new["x_position"] = alien_0_new["x_position"] + x_increment。
# 这个问题的根本原因在于，将完全不同性质的数据（描述性的字符串如 'speed' 和数值型的坐标如 'x_position'）混在一个字典里，导致了类型模糊。
# 更好的做法是使用一个更结构化的方式来组织数据，比如 Python 的 dataclass。这能从根源上消除类型歧义。
# 当数据结构变得复杂时，使用 dataclass 或自定义类来替代字典，能让代码更健壮、更易读，并从根本上避免类型混淆的问题。
"""
from dataclasses import dataclass

# 创建一个清晰的数据“蓝图”或“模板”
@dataclass
class Alien:
    x_position: int
    y_position: int
    speed: str

# 使用这个蓝图来创建外星人对象，类型非常清晰
alien_0 = Alien(x_position=0, y_position=25, speed="medium")
"""

print(f"New position: {alien_0_new['x_position']}")
# 使用了一个 if-elif-else 语句来确定外星人应该向右移动多远，并将这个值赋给变量 x_increment。
# 确定移动量后，将其与 x_position 的当前值相加，再将结果关联到字典中的键 x_position。
# 这种技巧很棒：通过修改外星人字典中的值，可改变外星人的行为。
alien_0["speed"] = "fast"


# 对于字典中不再需要的信息，可使用 del 语句将相应的键值对彻底删除。在使用 del 语句时，必须指定字典名和要删除的键。
alien_0 = {"color": "green", "points": 5}
print(alien_0)
del alien_0["points"]
print(alien_0)
# del 语句让 Python 将键 'points' 从字典 alien_0 中删除，同时删除与这个键关联的值。
# 删除的键值对永久消失了。

# 由类似的对象组成的字典
# 在前面的示例中，字典存储的是一个对象（游戏中的一个外星人）的多种信息，但也可以使用字典来存储众多对象的同一种信息。
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
# 假设要调查很多人，询问他们喜欢的编程语言，可使用一个字典来存储这种简单调查的结果。
# 将一个较大的字典放在了多行中。每个键都是一个被调查者的名字，而每个值都是被调查者喜欢的语言。
# 当确定需要使用多行来定义字典时，先在输入左花括号后按回车键，再在下一行缩进 4 个空格，
# 指定第一个键值对，并在它后面加上一个逗号。此后再按回车键，文本编辑器将自动缩进后续键值对，且缩进量与第一个键值对相同。
# 一种不错的做法是，在最后一个键值对后面也加上逗号，为以后添加键值对做好准备。
# 对于较长的列表和字典，大多数编辑器提供了以类似方式设置格式的功能。
# 对于较长的字典，还有其他一些可行的格式设置方式，因此在你的编辑器或其他源代码中，你可能会看到稍微不同的格式设置方式。

# 给定被调查者的名字，可使用这个字典轻松地了解他喜欢的语言：
language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")
# 创建这个新变量，使得函数调用 print()整洁得多。


# 使用get访问字典的值。字典的底层数据结构是哈希表，get 方法的平均时间复杂度是 O(1)。
# 使用放在方括号内的键从字典中获取感兴趣的值，可能会引发问题：如果指定的键不存在，就将出错。
alien_0 = {"color": "green", "speed": "slow"}
# print(alien_0["points"])
# KeyError: 'points'
# 可使用 get() 方法在指定的键不存在时返回一个默认值。
# get() 方法的第一个参数用于指定键，是必不可少的；第二个参数为当指定的键不存在时要返回的值，是可选的。

alien_0 = {"color": "green", "speed": "slow"}
point_value = alien_0.get("points", "No point value assigned.")
print(point_value)
# 如果指定的键有可能不存在，应考虑使用 get() 方法，而不要使用方括号表示法。
# 注意：在调用 get() 时，如果没有指定第二个参数且指定的键不存在，Python 将返回值 None，这个特殊的值表示没有相应的值，None 只是一个表示所需值不存在的特殊值。


# 一个 Python 字典可能只包含几个键值对，也可能包含数百万个键值对。鉴于字典可能包含大量数据，Python 支持对字典进行遍历。
# 字典可用于以各种方式存储信息，因此有多种遍历方式：既可遍历字典的所有键值对，也可只遍历键或值。
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# 可以用 for 循环来遍历字典的所有信息。
# 要编写遍历字典的 for 循环，可声明两个变量，分别用于存储键值对中的键和值。
# 这两个变量可以使用任意名称。下面的代码使用了简单的变量名，这完全可行：

for k, v in user_0.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

# for 语句的第二部分包含字典名和方法 items()，这个方法返回一个键值对列表（更严谨是一个字典视图对象）。
# 字典视图对象本身是一个可迭代对象，可以调用它的 iter() 函数，每次获得一个新的，独立的迭代器。
# 接下来，for 循环依次将每个键值对赋给指定的两个变量。
# 在这个示例中，使用这两个变量来打印每个键和与它关联的值。
# 第一个函数调用 print() 中的 "\n" 确保在输出每个键值对前插入一个空行：

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
# 变量命名为 name 和 language，可读性更强，使得循环的作用更容易理解。
# 这些描述性名称让人能够非常轻松地明白函数调用print() 是做什么的。

# 在不需要使用字典中的值时，keys() 方法很有用。下面来遍历字典favorite_languages，并将每个被调查者的名字都打印出来：
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())

# 在遍历字典时，会默认遍历所有的键。因此，上述代码输出不变。
# 如果显式地使用 keys() 方法能让代码更容易理解，就可以选择这样做，但如果你愿意，也可以省略它。
# 在这种循环中，可使用当前的键来访问与之关联的值。
# 创建一个包含要收到打印信息的朋友的列表。
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# 还可以使用 keys() 确定某个人是否接受了调查。
# keys() 方法并非只能用于遍历：实际上，它会返回一个列表，其中包含字典中的所有键。
# 在现代Python（Python 3）中，字典的 .keys() 方法返回的是一个特殊的“字典视图”对象（dictionary view object），它的类型是 dict_keys。
# 把这个“视图”对象想象成一个动态的、只读的、链接到原字典的“橱窗”。
# 当调用 .keys() 时，Python并没有创建一个新的列表，然后把所有的键都复制进去。
# 它只是创建了一个轻量级的“视图”对象，这个对象本身几乎不占用内存。它只是“看着”原始字典里的键。
# 它是动态的（Live View）这是“视图”对象和列表最本质的区别。
# 它提供字典的实时视图。如果您在原始字典中添加、更改或删除条目，视图对象将立即反映这些更改。
# 它是可迭代对象，可以多次循环访问它。
# dict_keys对象是可迭代的，所以您可以直接在 for 循环中使用它来遍历所有的键。
# dict_keys对象支持像 in 这样的成员检测，并且效率非常高（时间复杂度为O(1)），这和集合的特性很像。
# list(my_dict.keys())可以转换为列表。

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 遍历字典时将按插入元素的顺序返回其中的元素，但是在一些情况下，你可能要按与此不同的顺序遍历字典。
# 一种办法是在 for 循环中对返回的键进行排序。为此，可使用 sorted() 函数来获得按特定顺序排列的键列表的副本：
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
# 这条 for 语句类似于其他 for 语句，但对方法 dictionary.keys()的结果调用了 sorted() 函数。
# 这让 Python 获取字典中的所有键，并在遍历前对这个列表进行排序。输出表明，按字母顺序显示

# 如果你感兴趣的是字典包含的值，可使用 values() 方法。它会返回一个值列表，不包含任何键。
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


# 这种做法提取字典中所有的值，而没有考虑值是否有重复。
# 为剔除重复项，可使用集合（set）。集合中的每个元素都必须是独一无二的。
# 集合与列表的区别一个集合里的元素不允许重复，此外集合还是无序的。
# 不能通过下标来访问集合中的元素。
# 集合的主要操作不是访问单个元素，而是进行高效的成员资格测试（判断一个元素在不在集合里）。以及进行数学上的交集、并集、差集等运算。
# 集合也是基于哈希表，完全可以想象为一个只有键的字典。

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
# 通过将包含重复元素的列表(其实是动态的字典值的视图对象)传入 set()，可让 Python 找出列表中独一无二的元素，并使用这些元素来创建一个集合。
# 集合的构造函数从可迭代对象不断取出值，对每个值求哈希值，快速判断其是否已经在集合中，如果已经在，就丢弃重复的值。
# 你会经常发现 Python 内置的功能可帮助你以希望的方式处理数据。


# 可以使用一对花括号直接创建集合，并在其中用逗号分隔元素
languages = {"python", "rust", "python", "c"}
print(languages)
# 集合和字典很容易混淆，因为它们都是用一对花括号定义的。
# 当花括号内没有键值对时，定义的很可能是集合。不同于列表和字典，集合不会以特定的顺序存储元素。


# list, tuple, dict, set 全都是可迭代对象，都可以直接用在 for 循环中。
# 直接遍历一个字典时，遍历的是它的键（keys）。
# list, tuple, dict, set 这四种都属于“容器（Container）”数据类型。
# 它们会把所有元素都实实在在地存储在内存中。您可以把它们想象成一个装满了货物的“仓库”。

# 字典视图 (Dictionary Views - dict.keys(), dict.values(), dict.items())。
# 核心特点：动态链接性。它不是一个独立的数据副本，而是通向原始字典的一个“实时监控窗口”。
# 如果原始字典发生变化，这个“窗口”看到的内容会立刻跟着变。
# 可以重复遍历。因为视图本身不存储状态，它只是一个指向源头（字典）的“传送门”。
# 可以反复通过这个门去看里面的东西。类比：一个橱窗。您可以随时去看橱窗里有什么商品，
# 如果店员更换了商品，您下次再看，看到的就是新商品了。可以看无数次。

# 迭代器 (Iterators - zip对象, map对象, 生成器)
# 核心特点：一次性消费。迭代器内部有一个“状态指针”，记录着当前遍历到了哪个位置。
# 它只能向前，不能后退。一旦遍历完成，它就被耗尽了，变成空的了。
# 可以重复遍历吗：不可以。它就像一张已经检过的电影票，只能用一次。
# 类比：一条一次性的传送带。物品（数据）从传送带的一端传来，您在另一端逐个取走。取完后，传送带就空了，不会再有新的物品出现。

# 后两种都占用级小的内存空间O(1)
# 容器、字典视图和迭代器，它们都属于可迭代对象。for循环是通用于所有可迭代对象的统一操作方式。

# 下面讲解嵌套。
# 有时候，需要将多个字典存储在列表中或将列表作为值存储在字典中，这称为嵌套。
# 如何管理成群结队的外星人呢？一种办法是创建一个外星人列表，其中每个外星人都是一个字典，包含有关该外星人的各种信息。
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 更符合现实的情形是，外星人不止三个，而且每个外星人都是用代码自动生成的。
# 自动生成多个外星人。这些外星人都具有相同的特征，但在 Python 看来，每个外星人都是独立的，这让我们能够独立地修改每个外星人。
# 首先创建一个用于存储外星人的空列表。
aliens = []
# 每次循环都创建一个外星人，共创建 30 个绿色的外星人。
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
# 显示前 5 个外星人。
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人。结果显示确实创建了 30个外星人。
print(f"Total number of aliens: {len(aliens)}")

# 在什么情况下需要处理成群结队的外星人呢？想象一下，随着游戏的进行，有些外星人会变色且加快移动速度。
# 在必要时，可使用 for 循环和 if 语句来修改某些外形人的颜色。
# 例如，将前三个外星人修改为黄色、速度中等且值 10 分。
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:5]:
    print(alien)
print("...")
# 要改变前三个外星人的速度、颜色和得分，于是遍历一个只包含这些外星人的切片。
# if 语句确保只修改绿色的外星人。
# 可以进一步拓展这个循环，加入 elif 代码块。
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15
# 经常需要在列表中存储大量的字典，而且每个字典都包含特定对象的众多信息。
# 例如，为网站的每个用户创建一个字典，并将这些字典存储在一个名为 users 的列表中。
# 在这个列表中，所有字典的结构都相同，因此可遍历这个列表，并以相同的方式处理其中的每个字典。

# 在字典中存储列表.
# 有些时候，需要将列表存储在字典中，而不是将字典存储在列表中。
# 例如，如何描述顾客点的比萨呢？
# 如果使用列表，只能存储要添加的比萨配料；但如果使用字典，其中的配料列表就只是用来描述比萨的一个方面。
# 首先创建一个字典，其中存储了有关顾客所点比萨的信息。
# 一个键是 'toppings'，与之关联的值是一个列表，其中存储了顾客要求添加的所有配料。
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")
# 当函数调用 print() 中的字符串很长，需要分成多行书写时，可以在合适的位置分行，在每行末尾都加上引号。
# 并且对于除第一行外的其他各行，都在行首加上引号并缩进。这样，Python 将自动合并括号内的所有字符串。
# print(f"You ordered a {pizza['crust']}-crust pizza "
#     "with the following toppings:")
# 每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。

# 在本章前面有关喜欢的编程语言的示例中，如果将每个人的回答都存储在一个列表中，被调查者就可以选择多种喜欢的语言。
# 在这种情况下，当我们遍历字典时，与每个被调查者关联的都是一个语言列表，而不是一种语言。
# 在这里，与每个名字关联的值都是一个列表。请注意，有些人喜欢的语言只有一种，而有些人喜欢的不止一种。
favorite_languages_new: dict[str, list[str]] = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages_new in favorite_languages_new.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages_new:
        print(f"\t{language.title()}")
# 使用变量languages_new(改名只是为了符合静态类型检查) 来依次存储字典中的每个值，因为这些值都是列表。
# 在遍历字典的主循环中，使用另一个 for 循环来遍历每个人喜欢的语言列表。
# 为了进一步改进这个程序，可在遍历字典的 for 循环开头添加一条 if语句，通过查看 len(languages_new) 的值来确定当前的被调查者喜欢的语言是否有多种。
# 如果他喜欢的语言不止一种，就像以前一样显示输出；如果只有一种，就相应地修改输出的措辞（改成 is）。

# 列表和字典的嵌套层级不应太多。如果嵌套层级比前面的示例多得多，很可能有更简单的解决方案。

# 可以在字典中嵌套字典，但这样可能会让代码很快变得非常复杂。
# 如果有一网站有多个用户，每个用户都有独特的用户名，可在字典中将用户名作为键。
# 然后将每个用户的信息存储在一个字典中，并将该字典作为与用户名关联的值。
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # 访问内部的字典
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
# 请注意，表示每个用户的字典都有相同的结构，虽然 Python 并没有这样的要求，但这使得嵌套的字典处理起来更容易。
# 倘若表示每个用户的字典都包含不同的键，for 循环内部的代码将更复杂。
