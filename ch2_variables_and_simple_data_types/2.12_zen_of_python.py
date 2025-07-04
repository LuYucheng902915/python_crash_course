# 2-12. Zen of Python:
# Enter import this into a Python terminal session and skim through the additional principles.

# 经验丰富的程序员倡导尽可能避繁就简。
# The Zen of Python, by Tim Peters
# import this
# 小彩蛋，当您输入并执行这行代码后，就会显示 "The Zen of Python" 的全部内容。
# 是Python编程语言的核心设计哲学和指导原则的集合。
# 它不是强制的语法规则，而更像是一系列共19条的“箴言”或“警句”，用来引导开发者写出优雅、简洁、易于理解和维护的Python代码。
# 当你听到别人说某种写法“很Pythonic”（很符合Python风格），通常意味着这种写法遵循了“Python之禅”里的原则。

"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

"""
优美优于丑陋。
代码的优雅和美感很重要，应该追求编写漂亮的代码。

明确优于隐晦。
代码的意图应该清晰地表达出来，而不是依赖于隐晦的、需要猜测的规则。

简单优于复杂。
面对问题时，应优先选择简单的解决方案，而不是进行不必要的过度设计。

复杂优于繁复。
如果问题本身就很复杂，那么宁可接受一个结构化的复杂方案，也不要选择一个混乱、难以理解的繁复方案。

扁平优于嵌套。
代码结构应该尽可能扁平，避免过深的嵌套，因为深层嵌套会大大降低可读性。

稀疏优于密集。
代码行不应过于拥挤和密集，适当的留白和换行能让代码更易于阅读。

可读性很重要。
编写代码时必须时刻牢记，清晰易读是至关重要的，因为代码的读者远比作者多。

特例不应破坏规则。
为了一个特殊的边缘情况而破坏整体代码的优雅和一致性，通常是不值得的。

尽管实用性胜过纯粹性。
尽管规则很重要，但在面对现实问题时，一个能有效解决问题的实用方案比一个理论上完美但繁琐的纯粹方案更好。

错误不应悄然放过。
程序中的错误应该明确地暴露出来（比如抛出异常），而不是被隐藏或忽略掉，否则会埋下更大的隐患。

除非明确令其沉默。
如果你确实需要忽略一个错误，那么你的代码必须明确地（例如通过try...except）表达出“我知道这里有错误，我选择忽略它”的意图。

面对歧义，拒绝猜测的诱惑。
当遇到模棱两可、不明确的情况时，不要凭感觉猜测它的行为，而应该通过查阅文档或实验来获得确切的答案。

应存在一种——且最好只有一种——显而易见的解决方法。
对于一个问题，应该有一种清晰、直接、符合语言习惯的解决方案，让有经验的开发者都能想到一起去。

尽管这种方法一开始可能并不那么明显——除非你是荷兰人。
这句是对Python之父（荷兰人Guido van Rossum）的幽默致敬，意思是Python推崇的“显而易见”之道，有时也需要经验才能体会。

现在优于永不。
开始动手去做，远比因为追求完美而永远不动手要好。

尽管永不常常优于“草率”的现在。
但是，如果还没想清楚就开始草率行事，那么一个糟糕的实现还不如暂时不做。

如果实现难以解释，那么它就是个坏主意。
如果一个解决方案复杂到你自己都很难向别人解释清楚，那它很可能不是一个好的设计。

如果实现易于解释，那么它“可能”是个好主意。
反之，一个容易解释的实现方案，有更大的可能性是一个好主意。

命名空间是一种绝妙的理念——让我们多加利用吧！
通过模块、类等方式来组织和隔离变量名（即命名空间）是一个非常棒的设计，我们应该多加使用以避免命名冲突和混乱。
"""
