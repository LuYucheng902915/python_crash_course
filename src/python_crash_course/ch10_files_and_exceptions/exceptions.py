# Python 使用称为异常（exception）的特殊对象来管理程序执行期间发生的错误。
# 每当发生让 Python 不知所措的错误时，它都会创建一个异常对象。
# 如果编写了处理该异常的代码，程序将继续运行；如果你未对异常进行处理，程序将停止，并显示一个 traceback，其中包含有关异常的报告。
# 异常是使用 try-except 代码块处理的。
# try-except 代码块让 Python 执行指定的操作，同时告诉 Python 在发生异常时应该怎么办。
# 在使用 try-except 代码块时，即便出现异常，程序也将继续运行：显示编写的友好的错误消息，而不是令用户迷惑的 traceback。

# 处理 ZeroDivisionError 异常。
# 下面来看一种导致 Python 引发异常的简单错误。将数除以 0。
# print(5 / 0)
# Python 无法这样做，因此将看到一个 traceback：
# ZeroDivisionError: division by zero
# 在上述 traceback 中，错误 ZeroDivisionError 是个异常对象。
# Python 在无法按你的要求做时，就会创建这种对象。
# 在这种情况下，Python 将停止运行程序，并指出引发了哪种异常，可根据这些信息对程序进行修改。
# 下面将告诉 Python，在发生这种错误时该怎么办。这样，如果再次发生这样的错误，就有所准备了。
from pathlib import Path

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# 这里将导致错误的代码行 print(5/0) 放在一个 try 代码块中。
# 如果 try 代码块中的代码运行起来没有问题，Python 将跳过 except 代码块；如果 try 代码块中的代码导致错误，Python 将查找与之匹配的 except 代码块并运行其中的代码。
# 在这个示例中，try 代码块中的代码引发了 ZeroDivisionError 异常，因此 Python 查找指出了该怎么办的 except 代码块，并运行其中的代码。
# 这样，用户看到的是一条友好的错误消息，而不是 traceback。
# 如果 try-except 代码块后面还有其他代码，程序将继续运行，因为Python 已经知道了如何处理错误。


# 使用异常避免崩溃：如果在错误发生时，程序还有工作没有完成，妥善地处理错误就显得尤其重要。
# 这种情况经常出现在要求用户提供输入的程序中。如果程序能够妥善地处理无效输入，就能提示用户提供有效输入，而不至于崩溃。
"""
print("Give me two numbers, and I'll devide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break

    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    answer = int(first_number) / int(second_number)
    print(answer)
"""
# 这个程序没有采取任何处理错误的措施，因此在执行除数为 0 的除法运算时，它将崩溃。
# 程序崩溃可不好，让用户看到 traceback 也不是个好主意。
# 不懂技术的用户会感到糊涂，怀有恶意的用户还能通过 traceback 获悉不想让他们知道的信息。
# 例如，他们将知道程序文件的名称，还将看到部分不能正确运行的代码。
# 有时候，训练有素的攻击者可根据这些信息判断出可对你的代码发起什么样的攻击。

# 通过将可能引发错误的代码放在 try-except 代码块中，可提高程序抵御错误的能力。
# 因为错误是执行除法运算的代码行导致的，所以需要将它放到 try-except 代码块中。
# 这个示例还包含一个 else 代码块，只有 try 代码块成功执行才需要继续执行的代码，都应放到 else 代码块中：
print("Give me two numbers, and I'll devide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break

    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
# 让 Python 尝试执行 try 代码块中的除法运算，这个代码块只包含可能导致错误的代码。
# 依赖 try 代码块成功执行的代码都被放在 else 代码块中。
# 在这个示例中，如果除法运算成功，就使用 else 代码块来打印结果。
# except 代码块告诉 Python，在出现 ZeroDivisionError 异常时该怎么办。
# 如果 try 代码块因零除错误而失败，就打印一条友好的消息，告诉用户如何避免这种错误。
# 程序会继续运行，而用户根本看不到 traceback：
# 只有可能引发异常的代码才需要放在 try 语句中。
# 有时候，有一些仅在 try 代码块成功执行时才需要运行的代码，这些代码应放在 else 代码块中。
# except 代码块告诉 Python，如果在尝试运行 try 代码块中的代码时引发了指定的异常该怎么办。
# 通过预测可能发生错误的代码，可编写稳健的程序。
# 它们即便面临无效数据或缺少资源，也能继续运行，不受无意的用户错误和恶意攻击的影响。

# 处理 FileNotFoundError 异常。
# 在使用文件时，一种常见的问题是找不到文件：要查找的文件可能在其他地方，文件名可能不正确，或者这个文件根本就不存在。
# 对于所有这些情况，都可使用 try-except 代码块来处理。
# 来尝试读取一个不存在的文件。
"""
path = Path("alice.txt")
contents = path.read_text(encoding="utf-8")
"""
# 请注意，这里使用 read_text() 的方式与前面稍有不同。
# 如果系统的默认编码与要读取的文件的编码不一致，参数 encoding 必不可少。
# encoding 参数的作用是充当“翻译官”或“解码器”。
# 它告诉 Python 应该使用哪一套“密码本”来将硬盘上存储的原始字节（Bytes），转换成人类能阅读和理解的字符串（Characters）。
# 如何将毫无意义的数字 [228, 189, 160, ...] 变成能看懂的 "你好" 呢？这就需要一个翻译规则，这个规则就是编码 (Encoding)。
# Python 如果使用错误的解码器，就会得到乱码 (Mojibake)。
# 历史上，存在过很多种不同的编码标准，造成了混乱：
# 为了解决这个混乱，Unicode 标准诞生了。它致力于为世界上每一个字符都分配一个独一无二的编号。
# 而 UTF-8 就是目前最流行、最通用的，用来实现 Unicode 标准的一种编码方式。
# UTF-8 的优点:
# 全球通用: 它可以表示世界上几乎所有的字符，包括各种语言和表情符号。
# 向后兼容 ASCII: 所有的英文字符在 UTF-8 中都只占用1个字节，和 ASCII 完全一样。
# 互联网标准: 它是当今网页、API 等网络传输事实上的标准编码。
# 如果要读取的文件不是在你的系统中创建的，这种情况更容易发生。
# Python 无法读取不存在的文件，因此引发了一个异常：
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

# 下面介绍如何看懂复杂的 traceback。
# 通常最好从 traceback 的末尾着手。从最后一行可知，引发了异常 FileNotFoundError。
# 这一点很重要，它让我们知道应该在要编写的 except 代码块中使用哪种异常。
# 回头看看 traceback 开头附近，从这里可知，错误发生在文件 exceptions.py 的第 89 行。
# 接下来的一行列出了导致错误的代码行。
# traceback 的其余部分列出了一些代码，它们来自打开和读取文件涉及的库。
# 通常，不需要详细阅读和理解 traceback 中的这些内容。
# 为了处理这个异常，应将 traceback 指出的存在问题的代码行放到 try代码块中。
path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
# 在这个示例中，try 代码块中的代码引发了 FileNotFoundError 异常，因此要编写一个与该异常匹配的 except 代码块。
# 这样，当找不到文件时，Python 将运行 except 代码块中的代码，从而显示一条友好的错误消息，而不是 traceback。
# 如果文件不存在，这个程序就什么也做不了，因此上面就是这个程序的全部输出。
# 下面来扩展这个示例，看看当使用多个文件时，异常处理可提供什么样的帮助。

# 分析文本，可以分析包含整本书的文本文件。
# 很多经典文学作品是以简单的文本文件的方式提供的，因为它们不受版权限制。
# 本节使用的文本来自古登堡计划，该计划提供了一系列不受版权限制的文学作品。
# 如果你要在编程项目中使用文学文本，这是一个很不错的资源。
# 下面来提取童话 Alice in Wonderland（《爱丽丝漫游奇境记》）的文本，并尝试计算它包含多少个单词。
# 将使用 split() 方法，它默认以空白为分隔符将字符串分拆成多个部分：
path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
# 将文件 alice.txt 移到了正确的目录中，让 try 代码块能够成功地执行。
# 对变量 contents（它现在是一个长长的字符串，包含童话 Alice in Wonderland 的全部文本）调用 split() 方法，生成一个列表，其中包含这部童话中的所有单词。
# 通过对这个列表调用 len()，可知道原始字符串大致包含多少个单词。
# 最后，打印一条消息，指出文件包含多少个单词。
# 这些代码都放在 else 代码块中，因为仅当 try 代码块成功执行时才会执行它们。
# 输出指出了文件 alice.txt 包含多少个单词。


# 使用多个文件，下面多分析几本书。
# 先将这个程序的大部分代码移到一个名为 count_words() 的函数中，这样对多本书进行分析会更容易：
def count_words(path):
    """计算一个文件大致包含多少单词"""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


path = Path("alice.txt")
count_words(path)
# 这些代码大多与原来一样，只是被移到了函数 count_words() 中，并且增加了缩进量。
# 在修改程序的同时更新注释是个不错的习惯，因此将注释改成了文档字符串。
# 现在可以编写一个简短的循环，计算要分析的任何文本包含多少个单词了。
# 为此，把要分析的文件的名称存储在一个列表中，然后对列表中的每个文件都调用 count_words()。
# 将尝试计算 Alice in Wonderland、Siddhartha（《悉达多》）、Moby Dick（《白鲸》）和 Little Women（《小妇人》）分别包含多少个单词，它们都不受版权限制。
# 故意没有将 siddhartha.txt 放到 word_count.py 所在的目录中，以便展示这个程序在文件不存在时应对得如何：
filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]
for filename in filenames:
    path = Path(filename)
    count_words(path)
# 先将文件名存储为简单字符串，然后将每个字符串转换为 Path 对象，再调用 count_words()。
# 虽然文件 siddhartha.txt 不存在，但这丝毫不影响这个程序处理其他文件：
# 在这个示例中，使用 try-except 代码块有两个重要的优点：一是避免用户看到 traceback，二是让程序可以继续分析能够找到的其他文件。
# 如果不捕获因找不到 siddhartha.txt 而引发的 FileNotFoundError 异常，用户将看到完整的 traceback，而程序将在尝试分析 Siddhartha 后停止运行——根本不分析 Moby Dick 和 Little Women。


# 静默失败：在上一个示例中，告诉用户有一个文件找不到。
# 但并非每次捕获异常都需要告诉用户，有时候希望程序在发生异常时保持静默，就像什么都没有发生一样继续运行。
# 要让程序静默失败，可像通常那样编写 try 代码块，但在 except 代码块中明确地告诉 Python 什么都不要做。
# Python 有一个 pass 语句，可在代码块中使用它来让 Python 什么都不做：
def count_words_new(path):
    """计算一个文件大致包含多少单词"""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


for filename in filenames:
    path = Path(filename)
    count_words_new(path)
# 相比于上一个程序，这个程序唯一的不同之处是，except 代码块包含一条 pass 语句。
# 现在，当出现 FileNotFoundError 异常时，虽然仍将执行 except 代码块中的代码，但什么都不会发生。
# 当这种错误发生时，既不会出现 traceback，也没有任何输出。
# 用户将看到存在的每个文件包含多少个单词，但没有任何迹象表明有一个文件未找到：
# pass 语句还充当了占位符，提醒你在程序的某个地方什么都没有做，而且以后也许要在这里做些什么。
# 例如，在这个程序中，可能决定将找不到的文件的名称写入文件 missing_files.txt。
# 虽然用户看不到这个文件，但我们可以读取它，进而处理所有找不到文件的问题。


# 决定报告哪些错误:该在什么情况下向用户报告错误？又该在什么情况下静默失败呢？
# 如果用户知道要分析哪些文件，他们可能希望在有文件未被分析时出现一条消息来告知原因。
# 如果用户只想看到结果，并不知道要分析哪些文件，可能就无须在有些文件不存在时告知他们。
# 向用户显示他们不想看到的信息可能会降低程序的可用性。
# Python 的错误处理结构让程序员能够细致地控制与用户共享错误信息的程度，要共享多少信息由你决定。
# 编写得很好且经过恰当测试的代码不容易出现内部错误，如语法错误和逻辑错误，但只要程序依赖于外部因素，如用户输入、是否存在指定的文件、是否有网络连接，就有可能出现异常。
# 凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息。

# try...except 的基本工作流程：Python 首先会尝试执行 try 代码块里的所有代码。
# 一切顺利: 如果 try 块里的代码从头到尾都没有发生任何错误，那么所有的 except 块都会被完全跳过，程序继续执行 try...except 结构之后的代码。
# 发生错误: 如果在 try 块的任何一行代码上发生了一个错误（称之为“抛出异常”），那么：
# try 块中剩下的代码会立即被跳过，不再执行。
# Python 会拿着这个“异常对象”（比如 ZeroDivisionError），从上到下依次检查后面的 except 语句。
# 它会寻找第一个能够匹配该异常类型的 except 块。
# 一旦找到匹配的 except 块，它就会执行这个块里的代码。称之为捕获（Catch）异常。
# 一旦有一个 except 块捕获了异常，其他的 except 块就不再被检查了。执行完捕获块后，程序会继续执行整个 try...except 结构之后的代码。
# 在多级函数调用时，当一个错误发生时，它会首先在当前函数里寻找处理方案（try...except）。
# 如果当前函数处理不了，它就把这个“烂摊子”甩给调用它的上级函数，上级再找不到就再甩给它的上级，一直往上，直到找到能处理它的 except 块，或者整个程序崩溃。
# 可以自定义异常类，来更清晰表明发生的错误，比如特定的错误条件下，说明代码的逻辑问题。
# 异常类继承 Exception，通常只需要定义异常类的名字，里面的内容写 pass就可以。

# 在Python中，try...except...else...finally 提供了一套完整且强大的机制，用于处理程序在运行时可能出现的异常（错误），并确保关键的清理操作得以执行。
# 这个结构由四个可选的代码块组成，协同工作以实现健壮的程序流程控制。
# 该语法的核心始于 try 块，它的功能是包裹那些预期可能会出错的“危险”代码。
# 紧随其后的是一个或多个 except 块，它们是程序的“应急预案”或“安全网”。
# 每个 except 块都可以指定一种或多种它能处理的特定错误类型。
# 如果 try 块中的代码真的抛出了一个异常，Python 就会寻找能与该异常类型匹配的 except 块来执行，从而处理这个错误。
# 为了更清晰地分离成功和失败的逻辑，Python 提供了 else 块。
# 这个代码块的功能是定义只有在 try 块没有发生任何错误、顺利完成后才应该执行的“成功”逻辑。
# 最后，也是最特殊的部分，是 finally 块。它的功能是定义一段无论如何都必须执行的“最终清理”代码，其核心使命是确保像关闭文件、释放锁或断开网络连接这样的重要操作一定会被执行。
# 如果 try 块中的代码从头到尾顺利执行完毕，没有发生任何异常，那么程序的执行顺序是：try -> else -> finally。except 块会被完全跳过。执行完 finally 块之后，程序会继续执行整个结构之后的代码。
# 如果 try 块中途发生了一个异常，并且这个异常的类型与某个 except 块匹配，那么执行顺序是：try (发生错误处中断) -> 匹配的 except -> finally。try 块中剩下的代码和 else 块都会被跳过。
# 执行完 finally 块之后，程序同样会继续执行整个结构之后的代码。
# 发生错误但未被捕获，或遇到 return：最能体现 finally 独特价值的场景是当 try 块中发生未被捕获的异常（比如 except 指定的类型不匹配），或者在 try 或 except 块中遇到了 return 语句导致函数准备提前退出时。
# 在这种情况下，程序流程会立即准备跳转。
# 此时，else 块和整个结构之后的代码都不会被执行。然而，Python 保证 finally 块依然会在程序流程最终跳转之前被强制执行。
# 这确保了无论程序是以何种戏剧性的方式退出，最后的“关灯”、“锁门”等清理工作一定能完成。
# 总而言之，这四个部分各司其职：try 负责尝试危险操作，except 负责处理失败，else 负责庆祝成功，而 finally 则是不论成败、风雨无阻的“清道夫”，确保程序状态的干净和资源的释放。
# try, except, else, finally 这几个代码块共同构成一个单一的、不可分割的复合语句。不能在它们之间插入任何不相关的代码。
# try 是起点，任何这个结构都必须由一个 try 块开始。
# try 块不能“独活”，一个 try 块后面，必须跟着至少一个 except 块 或者一个 finally 块。它不能单独存在。
# try...finally：用途是不捕获任何错误，只是为了保证一段清理代码必定被执行。
# 不关心 try 块里发生了什么错误，也不想在这里处理它（可能会让更高层级的代码去处理）。
# 唯一的目标就是：无论发生什么，都必须把 finally 块代码执行掉。
# try...finally 结构完美地实现了这个需求。之前讨论的 with 语句，其本质就是这个 try...finally 结构的语法糖。

# 当 try 块中的代码顺利执行完毕、没有抛出任何异常时，程序的控制流便会首先进入 else 代码块（如果存在的话）。
# 现在，关键点来了：无论 else 块是如何结束的——无论是正常执行完毕，还是因为遇到了return, break, continue等控制流跳转语句而准备提前退出——程序都保证在真正跳转之前，必须先完整地执行 finally 块（如果存在的话）中的所有代码。
# 在 finally 块执行完毕后，程序才会根据 else 块中的指令决定下一步的走向。
# 如果 else 块中没有return等跳转语句，那么程序会继续执行整个 try...finally 结构之后的所有代码；反之，如果 else 块中有 return 语句，那么在执行完 finally 块之后，函数就会立即返回，结构之后的代码将不会被执行。
# 当 try 块中的代码执行时一旦碰到异常，程序的正常流程会立即中断，并跳过 try 块中余下的所有代码，此时else块也注定不会被执行。
# 紧接着，Python 会检查其后的 except 块，寻找第一个能与当前异常类型匹配的“捕获网”。
# 如果找到了匹配的 except块，程序就会执行该块内的错误处理代码；如果遍历完所有 except 块都未能找到匹配项，那么这个异常就会保持“未捕获”状态。
# 无论异常是否被成功捕获，接下来都会轮到 finally 块登场。finally 块提供了一个绝对的保证：它内部的清理代码必定会在程序决定下一步走向（是恢复正常流程还是向上传播异常）之前被执行。
# 在 finally 执行完毕后，如果异常之前已经被 except 块成功“消化”，那么程序就会恢复正常，继续执行整个 try...finally 结构之后的代码，就好像错误从未发生过一样。
# 反之，如果异常未被捕获，那么在 finally 执行完毕后，该异常会继续沿着函数调用栈向上“冒泡”传播，去更高层级寻找能够处理它的 try...except 结构，此时结构之后的代码将不会被执行。
# 需要特别注意的是，如果在 try、except 或 finally 块中遇到了 return 等跳转语句，finally 块依然会抢在跳转前执行，如果在 finally 块本身中使用了 return，它会覆盖掉任何正在传播的异常，这是一种应极力避免的危险写法。
# finally 的唯一使命应该是资源清理，而不应该包含任何改变程序正常控制流的语句。

# 当一个异常在一个深层函数（例如 函数C）中被抛出时，它会首先在函数 C 内部寻找能够处理它的 except 块。
# 如果找不到，函数 C 的执行就会立即中断，但在彻底退出前，它会先执行自己的 finally块（如果存在）以完成必要的清理。
# 随后，这个未被捕获的异常对象会沿着函数调用栈被“抛”回到上一级的调用者（函数 B），并精确地出现在当初调用函数C的那一行代码上。
# 现在，关键点来了：如果函数 B 中调用函数 C 的这行代码没有被一个能够处理该异常的 try...except 结构所包裹，那么函数 B 对这个“天降”的异常也同样无能为力。
# 因此，函数 B 的执行也会在这一刻立即中断，它同样会在执行完自己的 finally 块之后，将这个“烫手的山芋”原封不动地继续向上抛给它的调用者（函数A）。
# finally 子句在 Python 中不能独立存在，它必须是 try 复合语句的一部分。
# 这个“冒泡”传播的过程会持续下去，直到遇到一个能捕获它的 try...except 安全网为止。
# 如果这个异常一路“畅通无阻”地冒泡到了程序的顶层，都无人认领，那么 Python 解释器最终会接管，终止整个程序的运行，并向控制台打印出详细的错误回溯信息，清晰地展示出这个异常从发生到最终“逸出”所经过的完整函数调用路径。
# 这就是产生 traceback 的机制。
