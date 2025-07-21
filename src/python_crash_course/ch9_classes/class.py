# 面向对象编程（object-oriented programming，OOP）是最有效的软件编写方法之一。
# 在面向对象编程中，你编写表示现实世界中的事物和情景的类（class），并基于这些类来创建对象（object）。
# 在编写类时，你要定义一批对象都具备的通用行为。
# 在基于类创建对象时，每个对象都自动具备这种通用行为。
# 然后，你可根据需要赋予每个对象独特的个性。使用面向对象编程可模拟现实情景，逼真程度到达了令人惊讶的地步。

# 在 Python 中，实例一定是对象，但对象不一定是实例。
# 在 Python 中，万物皆对象 (Everything is an object)。
# 这是一个最核心的设计哲学。对象是内存中存储数据的一个基本单位，它有三个基本特征：
# 身份 (Identity)：它在内存中的唯一地址。
# 类型 (Type)：它是什么种类的数据，例如 int, str, list，或者我们自己定义的类。
# 值 (Value)：它所存储的具体数据。
# “对象”是一个通用术语，指代内存中所有的数据实体。

# 根据类来创建对象称为实例化，这让你能够使用类的实例（instance）。
# “实例”这个词的含义要更具体，它总是与“类”相关联。
# 实例是通过一个“类（Class）”作为模板或蓝图，被创建（或称作“实例化”）出来的具体实体。
# 在本章中，将编写一些类并创建其实例。
# 将指定可在实例中存储什么信息，定义可对这些实例执行哪些操作。
# 还将编写一些类来扩展既有类的功能，让相似的类能够共享功能，从而使用更少的代码做更多的事情。

# 模块 (Module)是一个 .py 文件，包含了相关的函数、类和变量。
# 导入入整个模块 (import 模块名)， 必须通过模块名. 的前缀来访问里面的任何内容（变量、函数、类）。
# 命名空间: 它只在你的主程序中创建了一个名字：模块名。所有的内容都封装在这个“模块名”命名空间里，不会和你的主程序中的名字冲突。
# 从模块中导入类或函数 (from 模块名 import ...)。
# 可以直接使用类和函数的名字，无需任何前缀。
# 直接把类和函数名字放进了主程序的命名空间，来源不清晰，可能导致命名混淆。

# 从模块 (Module) 到包 (Package)。
# 模块 (Module)：通常指一个单独的 .py 文件。
# 包 (Package)：是一个包含多个模块（或其他子包）的文件夹。这个文件夹之所以能被 Python 识别为一个“包”，是因为它内部包含一个特殊的文件：__init__.
# 当执行 import <包名> 时，Python 实际上会去执行这个包文件夹下的 __init__.py 文件。这个文件的主要作用是：
# 声明这是一个包：只要这个文件存在（哪怕是空的），Python 就会把这个文件夹当作一个包来对待。
# 构建包的命名空间：__init__.py 文件可以决定当用户导入这个包时，哪些东西（函数、类、变量）是“公开”的，可以直接通过包名. 来访问。
# 它就像一个“管家”，从各个房间（子模块）里拿出一些重要的东西，摆放在客厅（包的顶层命名空间）里，方便客人（用户）使用。
# 在文件系统中，如果它是一个 .py 文件，它就是“模块”。如果它是一个包含 __init__.py 文件的文件夹，它就是“包”（或“子包”）。
# 非常重要的一点是，import a.b 并不会把 b 这个名字直接放到你的当前可用列表里。
# 它只会在当前命名空间里创建顶级包的名字 a。你需要通过完整的路径来访问 b。
# 为了避免写很长的路径，我们经常使用 from 关键字。from 语句可以把子包或模块直接带到当前的命名空间。
# 把 import a.b.c 想象成一个邮寄地址 省.市.区：
# import a.b.c: 相当于你知道了 a 省 b 市 c 区 的完整地址，但每次寄信都得写全称。
# from a.b import c: 相当于你和 c 区建立了直接联系，以后可以直接说 c 区，不用再提省和市。
# 在一个 Python 文件中写下这两行代码时：import a, from a.b import c
# 主程序的命名空间中，会同时包含 a 和 c 这两个名字。

# 学习面向对象编程有助于像程序员那样看世界，并且真正明白编写的代码.
# 不仅是各行代码的作用，还有代码背后更宏大的概念。
# 了解类背后的概念可培养逻辑思维能力，让你能够通过编写程序来解决遇到的几乎任何问题。
# 随着面临的挑战日益严峻，类还能减轻你以及与你合作的其他程序员的负担。
# 如果你与其他程序员基于同样的逻辑来编写代码，你们就能明白彼此所做的工作。
# 你编写的程序将能被合作者理解，每个人都能事半功倍。

from random import choice, randint

import car5
import electric_car6 as ec
from car4 import Car4
from car5 import Car5, ElectricCar5
from electric_car6 import ElectricCar6
from electric_car6 import ElectricCar6 as EC


# 创建和使用类。使用类几乎可以模拟任何东西。
# 下面来编写一个表示小狗的简单类 Dog——它表示的不是特定的小狗，而是任何小狗。
# 由于大多数小狗具备两项信息（名字和年龄）和两种行为（坐下和打滚），Dog 类将包含它们。
# 这个类让 Python 知道如何创建表示小狗的对象。
# 编写这个类后，我们将使用它来创建表示特定小狗的实例。
# 创建 Dog 类，根据 Dog 类创建的每个实例都将存储名字和年龄，而且我们会赋予每条小狗坐下（sit()）和打滚（roll_over()）的能力。
class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


# 根据约定，在 Python 中，首字母大写的名称指的是类。
# 因为这是创建的全新的类，所以定义时不加括号。然后是一个文档字符串，对这个类的功能做了描述。

# __init__()方法，类中的函数称为方法。
# 前面学到的有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。
# __init__()是一个特殊方法，每当你根据 Dog 类创建新实例时，Python 都会自动运行它。
# 在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免 Python 默认方法与普通方法发生名称冲突。
# 务必确保 __init__() 的两边都有两个下划线，否则当你使用类来创建实例时，将不会自动调用这个方法，进而引发难以发现的错误。

# 在这个方法的定义中，形参 self 必不可少，而且必须位于其他形参的前面。
# 为何必须在方法定义中包含形参 self 呢？因为当 Python 调用这个方法来创建 Dog 实例时，将自动传入实参 self。
# 每个与实例相关联的方法调用都会自动传递实参 self，该实参是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
# 当创建 Dog 实例时，Python 将调用 Dog 类的__init__() 方法。
# 将通过实参向 Dog() 传递名字和年龄；self 则会自动传递，因此不需要传递。
# 每当根据 Dog 类创建实例时，都只需给最后两个形参（name 和 age）提供值。

# 在 __init__() 方法内定义的两个变量都有前缀 self。
# 以 self 为前缀的变量可供类中的所有方法使用，可以通过类的任意实例来访问。
# self.name = name 获取与形参 name 相关联的值，并将其赋给变量 name，然后该变量被关联到当前创建的实例。
# self.age = age 的作用与此类似。
# 像这样可通过实例访问的变量称为属性（attribute）。

# Dog 类还定义了另外两个方法：sit() 和 roll_over()。
# 由于这些方法执行时不需要额外的信息，因此只有一个形参 self。
# 稍后将创建的实例能够访问这些方法，换句话说，它们都会坐下和打滚。
# 当前，sit() 和 roll_over() 所做的有限，只是打印一条消息，指出小狗正在坐下或打滚。
# 但是可以扩展这些方法以模拟实际情况：
# 如果这个类属于一个计算机游戏，那么这些方法将包含创建小狗坐下和打滚动画效果的代码；如果这个类是用于控制机器狗的，那么这些方法将让机器狗做出坐下和打滚的动作。


# 可以将类视为有关如何创建实例的说明。例如，Dog 类就是一系列说明，让 Python 知道如何创建表示特定小狗的实例。
# 下面创建一个表示特定小狗的实例：
my_dog = Dog("Willie", 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
# 这里使用的是上一个示例中编写的 Dog 类。
# 让 Python 创建一条名字为 'Willie'、年龄为 6 的小狗。
# 在处理这行代码时，Python 调用Dog 类的 __init__() 方法，并传入实参 'Willie' 和 6。
# __init__() 方法创建一个表示特定小狗的实例，并且使用提供的值设置属性 name 和 age。
# 接下来，Python 返回一个表示这条小狗的实例，将这个实例赋给变量 my_dog。
# 在这里，命名约定很有用：通常可以认为首字母大写的名称（如 Dog）指的是类，而全小写的名称（如 my_dog）指的是根据类创建的实例。

# 要访问实例的属性，可使用点号。
# 点号在 Python 中很常用，这种语法演示了 Python 如何获取属性的值。
# 在这里，Python 先找到实例 my_dog，再查找与这个实例相关联的属性 name。
# 在 Dog 类中引用这个属性时，使用的是 self.name。用同样的方法来获取属性 age 的值。

# 调用方法根据 Dog 类创建实例后，就能使用点号来调用 Dog 类中定义的任何方法了。
my_dog.sit()
my_dog.roll_over()
# 要调用方法，需指定实例名（这里是 my_dog）和想调用的方法，并用句点分隔。
# 在遇到代码 my_dog.sit() 时，Python 在类 Dog 中查找方法 sit() 并运行其代码。
# 这种语法很有用。如果给属性和方法指定了合适的描述性名称，即便对于从未见过的代码块，也能够轻松地推断出它是做什么的。

# 可按需求根据类创建任意数量的实例。
your_dog = Dog("Lucy", 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
# 在这个示例中创建了两条小狗，分别名为 Willie 和 Lucy。
# 每条小狗都是一个独立的实例，有自己的一组属性，能够执行相同的操作。
# 即使给第二条小狗指定同样的名字和年龄，Python 也会根据 Dog 类创建另一个实例。
# 可以按需求根据一个类创建任意数量的实例，只要能给每个实例起一个独特的变量名，或者让它在列表或字典中占有一席之地就行。


# 可以使用类来模拟现实世界中的很多情景。
# 类编写好后，大部分时间将花在使用根据类创建的实例上。
# 需要完成的首要任务之一是，修改实例的属性。
# 既可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。


# 下面编写一个表示汽车的类，它存储了有关汽车的信息，并提供了一个汇总这些信息的方法。
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
# __init__() 方法接受这些形参的值，并将它们赋给根据这个类创建的实例的属性。
# 在创建新的 Car 实例时，需要指定其制造商、型号和生产年份。
# 定义一个名为 get_descriptive_name() 的方法，它使用属性 year、make 和 model 创建一个对汽车进行描述的字符串，无须分别打印每个属性的值。
# 为了在这个方法中访问属性的值，使用了 self.make、self.model 和 self.year。
# 有些属性无须通过形参来定义，可以在 __init__() 方法中为其指定默认值。


# 下面来添加一个名为 odometer_reading 的属性，其初始值总是为 0。
# 还添加了一个名为 read_odometer() 的方法，用于读取汽车的里程表：
class Car1:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car1 = Car1("audi", "a4", 2024)
print(my_new_car1.get_descriptive_name())
my_new_car1.read_odometer()
# 调用 __init__() 方法创建新实例时，将像上一个示例一样以属性的方式存储制造商、型号和生产年份。
# 接下来，Python 创建一个名为 odometer_reading 的属性，并将其初始值设置为 0。

# 可以用三种不同的方式修改属性的值：直接通过实例修改，通过方法设置，以及通过方法递增（增加特定的值）。
# 要修改属性的值，最简单的方式是通过实例直接访问它。
# 这里使用点号直接访问并设置汽车的属性 odometer_reading。
my_new_car1.odometer_reading = 23
my_new_car1.read_odometer()


# 有一个替你更新属性的方法大有裨益。这样就无须直接访问属性了，而是可将值传递给方法，由它在内部进行更新。
class Car2:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car2 = Car2("audi", "a4", 2024)
print(my_new_car2.get_descriptive_name())
my_new_car2.update_odometer(23)
my_new_car2.read_odometer()
my_new_car2.update_odometer(20)
my_new_car2.read_odometer()
# 添加了 update_odometer() 方法。这个方法接受一个里程值，并将其赋给self.odometer_reading。
# 通过实例 my_new_car 调用update_odometer()，并向它提供了实参 23（该实参对应于方法定义中的形参 mileage）。
# 这将里程表读数设置为 23。
# 还可以对 update_odometer() 方法进行扩展，使其在修改里程表读数时做些额外的工作。
# 添加了禁止将里程表读数往回调的逻辑。


# 有时候需要将属性值递增特定的量，而不是将其设置为全新的值。
# 假设我们购买了一辆二手车，从购买到登记期间增加了 100 英里的里程。
class Car3:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        让里程表读数增加指定的量
        """
        self.odometer_reading += miles


my_used_car = Car3("subaru", "outback", 2019)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# 新增的方法 increment_odometer() 接受一个单位为英里的数，并将其加到 self.odometer_reading 上。
# 可以修改这个方法，以禁止增量为负值，从而防止有人利用它把里程表往回调。
# 虽然可以使用类似于上面的方法来控制用户修改属性值的方式，但能够访问程序的人都能直接访问属性将其修改为任意的值。
# 要确保安全，除了进行类似于前面的基本检查以外，还需要极度关注细节。

# 继承：在编写类时，并非总要从头开始。如果要编写的类是一个既有的类的特殊版本，可使用继承（inheritance）。
# 当一个类继承另一个类时，将自动获得后者的所有属性和方法。
# 原有的类称为父类（parent class），而新类称为子类（child class）。
# 子类不仅继承了父类的所有属性和方法，还可定义自己的属性和方法。

# 子类的 __init__() 方法，在既有的类基础上编写新类，通常要调用父类的 __init__ 方法。
# 这将初始化在父类的 __init() 方法中定义的所有属性，从而让子类也可以使用这些属性。
# 方法是“根据定义”继承的。子类从定义的那一刻起就可以访问其父类的方法。
# 属性是“通过执行”创建的。只有当分配属性的代码实际运行时，实例才会获取属性。
# 子类继承其父类的所有方法。但是，要使子类实例继承其父类的属性，必须在子类的初始化过程中调用 __init__ 父类的方法，通常通过 super().__init__()。
# 这是处理继承的标准且正确的方法。调用父类的初始化方法，然后添加子类特有的属性。
# Python 中强烈推荐的最佳实践是在 __init__  方法内部初始化实例的所有属性。
# 即使属性的“真实”值稍后仅在另一种方法中确定，您仍应__init__使用默认值或占位符值（如 None、0 或空列表 []）来声明它。
# 下面来模拟电动汽车，这是一种特殊的汽车。因此可在之前的 Car 类的基础上创建新类，只需为电动汽车特有的属性和行为编写代码即可。


class ElectricCar(Car3):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
# 在创建子类时，父类必须包含在当前文件中，且位于子类前面。
# 在定义子类时，必须在括号内指定父类的名称。__init__() 方法接受创建 Car3 实例所需的信息。
# super() 是一个特殊的函数，能够调用父类的方法。
# 这行代码让 Python 调用 Car3 类的 __init__() 方法，从而让 ElectricCar 实例包含这个方法定义的所有属性。
# 父类也称为超类（superclass），函数名 super 由此得名。
# 为测试继承能正确发挥作用，尝试创建一辆电动汽车，但提供的信息与创建燃油汽车相同。
# 创建燃油汽车的一个实例，并将其赋给变量 my_leaf。
# 这行代码调用 ElectricCar 类中定义的__init__() 方法，后者让 Python 调用父类 Car 中定义的 __init__()方法。


# 给子类定义属性和方法。
# 让一个类继承另一个类后，就可以添加区分子类和父类所需的新属性和新方法了。
class ElectricCar1(Car3):
    def __init__(self, make, model, year):
        """先初始化父类的属性，再初始电动汽车独有的属性"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_leaf1 = ElectricCar1("nissan", "leaf", 2024)
print(my_leaf1.get_descriptive_name())
my_leaf1.describe_battery()
# 添加新属性 self.battery_size，并设置其初始值（40）。
# 根据 ElectricCar 类创建的所有实例都将包含这个属性，但所有的 Car 实例都不包含它。
# 对于 ElectricCar 类的特殊程度没有任何限制，在模拟电动汽车时，可根据所需的准确程度添加任意数量的属性和方法。
# 如果一个属性或方法是所有汽车都有的，而不是电动汽车特有的，就应将其加入 Car 类而不是 ElectricCar 类。
# 这样，使用 Car 类的成员将获得相应的功能，而 ElectricCar 类只包含处理电动汽车特有属性和行为的代码。


# 重写父类中的方法。
# 假设 Car 类有一个名为 fill_gas_tank() 的方法，它对电动汽车来说毫无意义，因此你可能想重写它。下面演示了一种重写方式：
class ElectricCar2(Car3):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")


# 现在，如果有人对电动汽车调用 fill_gas_tank() 方法，Python 将忽略 Car 类中的 fill_gas_tank() 方法，转而运行上述代码。
# 在使用继承时，可让子类保留从父类那里继承的“精华”，重写不需要的“糟粕”。


# 将实例用作属性。
# 在使用代码模拟实物时，你可能会发现自己给类添加了太多细节：属性和方法越来越多，文件越来越长。
# 在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。
# 将大型类拆分成多个协同工作的小类，这种方法称为组合（composition）。
class Battery:
    """一次模拟的电动汽车电池的简单尝试"""

    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar3(Car3):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """先初始化父类的属性。再初始化电动汽车独有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf2 = ElectricCar3("nissan", "leaf", 2024)
print(my_leaf2.get_descriptive_name())
my_leaf2.battery.describe_battery()
# 定义了一个名为 Battery 的新类，它没有继承任何类。
# __init__() 方法在 self 之外还有一个形参 battery_size。
# 这个形参是可选的：如果没有给它提供值，电池容量将被设置为 40。
# describe_battery() 方法也被移到了这个类中。

# 在 ElectricCar 类中，添加一个名为 self.battery 的属性。
# 这行代码让 Python 创建一个新的 Battery 实例（因为没有指定容量，所以为默认值 40），并将该实例赋给属性 self.battery。
# 每当__init__() 方法被调用时，都将执行该操作，因此现在每个 ElectricCar实例都包含一个自动创建的 Battery 实例。

# 创建一辆电动汽车，并将其赋给变量 my_leaf2。
# 在描述电池时，需要使用电动汽车的属性 battery：
# 这行代码让 Python 在实例 my_leaf 中查找属性 battery，并对存储在该属性中的 Battery 实例调用 describe_battery() 方法。
# 这看似做了很多额外的工作，但是现在想多详细地描述电池都可以，且不会导致 ElectricCar 类混乱不堪。


# 下面再给 Battery 类添加一个方法，它根据电池容量报告汽车的续航里程：
class Battery1:
    """一次模拟的电动汽车电池的简单尝试"""

    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条信息，指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar4(Car3):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """先初始化父类的属性。再初始化电动汽车独有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery1()


my_leaf3 = ElectricCar4("nissan", "leaf", 2024)
print(my_leaf3.get_descriptive_name())
my_leaf3.battery.describe_battery()
my_leaf3.battery.get_range()


# 导入类。随着不断地给类添加功能，文件可能变得很长，即便妥善地使用了继承和组合亦如此。
# 遵循 Python 的整体理念，应该让文件尽量整洁。
# Python 在这方面提供了帮助，允许你将类存储在模块中，然后在主程序中导入所需的模块。

# 下面创建一个只包含 Car4 类的模块
# from car4 import Car4

my_new_car3 = Car4("audi", "a4", "2024")
print(my_new_car3.get_descriptive_name())

my_new_car3.odometer_reading = 23
my_new_car3.read_odometer()
# import 语句让 Python 打开模块 car4 并导入其中的 Car4 类。
# 这样，就可以使用 Car4 类，就像它是在当前文件中定义的一样。
# 导入类是一种高效的编程方式。如果这个程序包含整个 Class 类，它会非常长。
# 通过将这个类移到一个模块中并导入该模块，依然可使用其所有功能，但主程序文件变得整洁易读了。
# 这还让你能够将大部分逻辑存储在独立的文件中。
# 在确定类能像你希望的那样工作后，就可以不管这些文件，专注于主程序的高级逻辑了。


# 尽管同一个模块中的类之间应该存在某种相关性，但其实可以根据需要在一个模块中存储任意数量的类。
# Battery1 类和 ElectricCar5 类都可帮助模拟汽车，下面将它们都加入模块 car5.py：
# from car5 import ElectricCar5
my_leaf4 = ElectricCar5("nissan", "leaf", 2024)
print(my_leaf4.get_descriptive_name())
my_leaf4.battery.describe_battery()
my_leaf4.battery.get_range()
# 此时输出与之前相同，但是大部分逻辑隐藏在 car5 模块中。
# 从一个类中导入多个类。可以根据需要在程序文件中导入任意数量的类。
# 如果要在同一个程序中创建燃油汽车和电动汽车，就需要将 Car5 类和 ElectricCar5 类都导入。
# from car5 import Car5, ElectricCar5
# 当从一个模块中导入多个类时，用逗号分隔各个类。导入必要的类后，就可根据需要创建每个类的任意数量的实例了。
my_mutsang = Car5("ford", "mutsang", 2024)
print(my_mutsang.get_descriptive_name())
my_leaf5 = ElectricCar5("nissan", "leaf", "2024")
print(my_leaf5.get_descriptive_name())

# 还可以先导入整个模块，再使用点号访问需要的类。这种导入方法很简单，代码也易读。
# 由于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。
# import car5
my_mutsang1 = car5.Car5("ford", "mutsang", 2024)
print(my_mutsang1.get_descriptive_name())
my_leaf6 = car5.ElectricCar5("nissan", "leaf", "2024")
print(my_leaf6.get_descriptive_name())
# 首先，导入整个 car5 模块。接下来，使用语法 module_name.classname 访问需要的类。实现了相同功能。

# 要导入模块中的每个类，可使用下面的语法：
# from module_name import *
# 不推荐这种导入方式，原因有二。
# 第一，最好只需要看一下文件开头的import 语句，就能清楚地知道程序使用了哪些类。
# 但这种导入方式没有明确地指出使用了模块中的哪些类。
# 第二，这种导入方式还可能引发名称方面的迷惑。
# 如果不小心导入了一个与程序文件中的其他东西同名的类，将引发难以诊断的错误。
# 这里之所以介绍这种导入方式，是因为虽然不推荐，但你可能在别人编写的代码中见到它。
# 当需要从一个模块中导入很多类时，还是最好在导入整个模块之后使用 module_name.classname 语法来访问这些类。
# 这样，虽然文件开头并没有列出用到的所有类，但是你清楚地知道在程序的哪些地方使用了导入的模块。
# 此外，这还避免了导入模块中的每个类可能引发的名称冲突。


# 在一个模块中导入另一个模块。
# 有时候，需要将类分散到多个模块中，以免模块太大或者在同一个模块中存储不相关的类。
# 在将类存储在多个模块中时，你可能会发现一个模块中的类依赖于另一个模块中的类。在这种情况下，可在前一个模块中导入必要的类。
# 下面将 Car4 类存储在一个模块中，并将 ElectricCar6 和 Battery2 类存储在另一个模块中。
# ElectricCar6 类需要访问其父类 Car4，因此直接将 Car4 类导入该模块。
# 现在可分别从每个模块中导入类，以根据需要创建任意类型的汽车了。
# from car4 import Car4
# from electric_car6 import ElectricCar6
my_mutsang2 = Car4("ford", "mutsang", "2024")
print(my_mutsang2.get_descriptive_name())
my_leaf7 = ElectricCar6("nissan", "leaf", "2024")
print(my_leaf7.get_descriptive_name())


# 使用别名，当使用模块来组织项目代码时，别名能发挥很大的作用。在导入类时，也可以给它指定别名。
# 假设要在程序中创建大量电动汽车实例，需要反复输入 ElectricCar，非常烦琐。
# 为了避免这种烦恼，可在 import 语句中给 ElectricCar 指定一个别名：
# from electric_car6 import ElectricCar6 as EC
# 现在每当需要创建电动汽车实例时，都可使用这个别名：
my_leaf8 = EC("nissan", "leaf", 2024)
print(my_leaf8.get_descriptive_name())
# 还可以给模块指定别名。下面导入模块 electric_car6 并给它指定了别名：
# import electric_car6 as ec
# 现在可以结合使用模块别名和完整的类名了：
my_leaf9 = ec.ElectricCar6("nissan", "leaf", 2024)
print(my_leaf9.get_descriptive_name())

# 在组织大型项目的代码方面，Python 提供了很多选项。
# 熟悉所有这些选项很重要，这样才能确定哪种项目组织方式是最佳的，才能理解别人开发的项目。
# 一开始应让代码结构尽量简单。
# 首先尝试在一个文件中完成所有的工作，确定一切都能正确运行后，再将类移到独立的模块中。
# 如果你喜欢模块和文件的交互方式，可在项目开始时就尝试将类存储到模块中。
# 先找出让你能够编写出可行代码的方式，再尝试让代码更加整洁。

# Python 标准库是一组模块，在安装 Python 时已经包含在内。
# 现在已经对函数和类的工作原理有了大致的了解，可以开始使用其他程序员编写好的模块了。
# 可以使用标准库中的任何函数和类，只需在程序开头添加一条简单的 import 语句即可。
# 下面来看看模块 random，它在你模拟很多现实情况时很有用。
# 在这个模块中，一个有趣的函数是 randint()。
# 它将两个整数作为参数，并随机返回一个位于这两个整数之间（含）的整数。
# 下面演示了如何生成一个位于 1 和 6 之间的随机整数：
# from random import randint
print(randint(1, 6))
# 在模块 random 中，另一个很有用的函数是 choice()。
# 它将一个列表或元组作为参数，并随机返回其中的一个元素：
# from random import choice
players = ["charles", "martina", "michael", "florence", "eli"]
print(choice(players))
# 在创建与安全相关的应用程序时，不要使用模块 random，但它能用来创建众多有趣的项目。
# random 生成的数字并不是真正意义上的随机，而是伪随机数（Pseudorandom Numbers）。
# 这意味着它们是通过一个确定性的算法计算出来的。这个算法的核心是一个被称为种子（seed）的初始值。
# 一旦种子确定，后续生成的“随机”序列实际上是完全固定的。
# Python 的 random 主要模块使用了马特赛特旋转演算算法（Mersenne Twister）作为其核心生成器。
# 虽然这个算法非常出色，能够生成在统计学上表现良好的高质量随机数序列，但作为它的致命弱点却具有其确定性。
# 如果攻击者能够知道或者猜测到原始的种子，他们就可以完全预测出接下来的整个随机数序列。
# 还可以从其他地方下载外部模块。第二部分的每个项目都需要使用外部模块，届时将看到很多这样的示例。


# 必须熟悉有些与类相关的编程风格问题，在编写的程序较复杂时尤其如此。
# 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，并且不使用下划线。
# 实例名和模块名都采用全小写格式，并在单词之间加上下划线。
# 对于每个类，都应在类定义后面紧跟一个文档字符串。
# 这种文档字符串简要地描述类的功能，应该遵循编写函数的文档字符串时采用的格式约定。
# 每个模块也都应包含一个文档字符串，对其中的类可用来做什么进行描述。
# 可以使用空行来组织代码，但不宜过多。
# 在类中，可以使用一个空行来分隔方法；而在模块中，可以使用两个空行来分隔类。
# 当需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的 import 语句，再添加一个空行，然后编写导入自己编写的模块的import 语句。
# 在包含多条 import 语句的程序中，这种做法让人更容易明白程序使用的各个模块来自哪里。
