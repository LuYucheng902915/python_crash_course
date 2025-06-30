# 列表（list）由一系列按特定顺序排列的元素组成,其中的元素之间可以没有任何关系。
# 列表的元素可以是任意类型的对象，包括数字、字符串、甚至其他列表。
# 在 Python 中，用方括号（[]）表示列表，用逗号分隔其中的元素。

bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)  # ，Python 将打印列表的内部表示，包括方括号和逗号。

# 列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置（索引）告诉 Python 即可。
# 要访问列表元素，可指出列表的名称，再指出元素的索引，并将后者放在方括号内。

print(bicycles[0])  # 输出第一个元素,只返回列表中元素，而不返回方括号和逗号。
print(bicycles[0].title())


print(bicycles[1])
print(bicycles[3])  # 索引从 0 开始，因此 bicycles[1] 返回列表中的第二个元素
print(bicycles[-1])  # 负数索引从列表末尾开始计数，-1 返回最后一个元素
print(bicycles[-2])  # -2 返回倒数第二个元素

# 可以像使用其他变量一样使用列表中的各个值

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)  # 输出：My first bicycle was a Trek.

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)
# 要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
# 字符串是不可变对象，列表是可变对象
# 在Python中，字符串 (str)、整数 (int)、元组 (tuple) 都是不可变的。
# 这意味着一旦创建了这些对象，就无法修改它们的内容。
# 如果你想“修改”它，唯一的方法是找一块新石碑，刻上新内容，然后把旧石碑的标签（变量名）贴到新石碑上。旧石碑本身没有变。
# 例如my_string = "hello"是创建了一个字符串对象，my_string[0] = "H"会报错，因为字符串是不可变的。
# my_string = my_string + " world"
# 当我们执行 my_string + " world" 时，Python并没有改变原来的 "hello" 石碑。它是在内存中创建了一块全新的石碑，
# 内容是 "hello world"，然后把 my_string 这个标签从旧石碑上撕下来，贴到了新石碑上。
# 通过 id() 函数可以看到，内存地址已经改变了，证明了这是一个全新的对象。

# 创建一块名为 my_string 的“石碑”，刻上 "hello"
my_string = "hello"
print(f"初始字符串: {my_string}, 内存地址 (id): {id(my_string)}")

# 尝试修改石碑的第一个字（会直接报错！）
try:
    my_string[0] = "H"
except TypeError as e:
    print(
        f"\n试图修改时出错: {e}"
    )  # 输出：'str' object does not support item assignment

# 当你“修改”字符串时，实际上是创建了一块新石碑
my_string = my_string + " world"
print(f"\n“修改”后的字符串: {my_string}, 新的内存地址 (id): {id(my_string)}")

# 可变对象 (Mutable) - 像一块可以随意擦写的白板
# 你可以在这块白板上随时增加、删除或修改内容。
# 无论你怎么修改，这块白板本身还是原来那块白板，它的内存地址没有变。
# 在Python中，列表 (list)、字典 (dict)、集合 (set) 都是可变的。

# 创建一块名为 my_list 的“白板”，写上 [1, 2, 3]
my_list = [1, 2, 3]
print(f"初始列表: {my_list}, 内存地址 (id): {id(my_list)}")

# 1. 在白板上修改第一个数字
my_list[0] = 99
print(f"修改元素后: {my_list}, 内存地址 (id): {id(my_list)}")

# 2. 在白板末尾添加一个新数字
my_list.append(4)
print(f"添加元素后: {my_list}, 内存地址 (id): {id(my_list)}")
print("\n")

# 函数传参: 如果你把一个列表传入一个函数，函数内部对列表的修改会影响到函数外部的原始列表（因为操作的是同一个“白板”）。而修改字符串则不会。
# 性能: 对于需要频繁增删改的操作，使用列表这样的可变对象效率更高，因为它避免了反复创建新对象。
# 字典的键 (Dictionary Keys): 字典的键必须是不可变类型。所以你可以用字符串或元组作为键，但不能用列表作为键。因为字典依赖哈希值工作，哈希值不可变。

# 创建三个独立的整数对象
a = 10
b = 20
c = 30

# 创建一个列表，它的元素是上面三个变量
my_list = [a, b, c]

# 打印列表本身和它内部元素的内存地址，id官方定义是返回对象的一个标识符，该标识符在对象生命周期唯一且恒定。与地址有一定区别。
print(f"列表 my_list 的内存地址: {id(my_list)}")
print("---")
print(f"整数 10 的内存地址: \t{id(a)}")
print(f"列表第一个元素的地址: \t{id(my_list[0])}")
print("---")
print(f"整数 20 的内存地址: \t{id(b)}")
print(f"列表第二个元素的地址: \t{id(my_list[1])}")
print("---")
my_list = [10, 20, 30]

print(f"修改前，列表的地址: \t{id(my_list)}")
print(f"修改前，第一个元素的地址: \t{id(my_list[0])}")
print("-" * 20)

# 现在，我们修改列表的第一个元素
# 这会在内存中创建一个新的整数对象 99
my_list[0] = 99

print(f"修改后，列表的地址: \t{id(my_list)}")  # <-- 地址不会变
print(f"修改后，第一个元素的地址: \t{id(my_list[0])}")  # <-- 地址会变
print(f"新的整数对象 99 的地址: \t{id(99)}")

# 上面体现了列表可变，整数不可变。列表的内容其实是各个对象的地址。

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)
# append() 方法在列表末尾添加新元素。

motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)
# insert() 方法在指定位置插入新元素，第一个参数是索引，第二个参数是要插入的值。
# insert() 方法在索引 0 处添加空间，并将值 'ducati' 存储到这个地方

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)
# del 语句删除列表中已知位置的元素。

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# 有时候，你要将元素从列表中删除，并接着使用它的值。例如，你可能要获取刚被消灭的外星人的x坐标和y坐标，
# 以便在相应的位置显示爆炸效果；在 Web 应用程序中，你可能要将用户从活动成员列表中删除，并将其加入非活动成员列表。
# pop() 方法删除列表末尾的元素，并将其值返回。删除列表尾元素相当于弹出栈顶元素
# 你依然能访问被删除的元素的值。
# 方法 pop() 有什么用处呢？假设列表中的自行车是按购买时间存储的，就可使用方法 pop() 来打印一条消息，指出最后购买的是哪款自行车
# 实际上，也可以使用 pop() 删除列表中任意位置的元素，只需要在括号中指定要删除的元素的索引即可。

motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)
# remove() 方法根据值删除列表中的元素，而不是根据索引。
# remove() 方法只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环，确保将每个值都删除。
# 使用 remove() 从列表中删除元素后，也可继续使用它的值。

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"

# Python在内存中创建了一个字符串对象 'ducati'。Python创建了一个列表对象 motorcycles，
# 它的第四个元素（索引为3）是一个指针，指向了 'ducati' 对象的内存地址。
# 当你执行 too_expensive = 'ducati' 时，Python非常聪明，它会发现内存中已经有一个内容为 'ducati' 的字符串对象了（这被称为字符串驻留/String Interning），
# 所以它不会创建新对象，而是让 too_expensive 这个变量也指向同一个内存地址。
# 下面是验证代码，motorcycles[3] 和 too_expensive 是指向同一个对象的两个不同的“指针”或“标签”。

print(f"列表第四个元素的内存地址: {id(motorcycles[3])}")
print(f"变量 too_expensive 的内存地址: {id(too_expensive)}")
print(f"它们指向同一个对象吗? {id(motorcycles[3]) == id(too_expensive)}")


motorcycles.remove(too_expensive)
# 它的作用是：在 motorcycles 这个列表中，找到第一个指向 'ducati' 对象的指针，然后把这个指针从列表中移除。
# 这个操作完全没有触碰到内存中那个 'ducati' 字符串对象本身，更没有影响到 too_expensive 这个变量。
# 此时，'ducati' 仍然存在于内存中，并且 too_expensive 仍然指向它。
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
# sort() 方法对列表进行永久性排序。它会直接修改原列表，而不是返回一个新的列表。

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reversed sorted list:")
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars)
# sorted() 函数对列表进行临时排序。它返回一个新的列表，而不修改原列表。

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)
# reverse() 方法对列表进行永久性反转。它会直接修改原列表，而不是返回一个新的列表。但又容易恢复，再使用reverse() 方法即可。

cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))
# len() 函数返回列表的长度，即列表中元素的个数。

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])
# 索引错误 list index out of range

# motorcycles = []
# print(motorcycles[-1])
# 索引错误 list index out of range
