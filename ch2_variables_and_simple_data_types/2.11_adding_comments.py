# 2-11. Adding Comments:
# Choose two of the programs you’ve written, and add at least one comment to each.
# If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file.
# Then write one sentence describing what the program does.

# 向大家问好。
print("Hello Python people!")

name = "eric"
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)
# {}一定要与f字符串一起使用。

# 随着程序越来越大、越来越复杂，就应该在其中添加说明，对你解决问题的方式进行大致的阐述。
# 注释(comment)让你能够使用自然语言在程序中添加说明。
# 编写注释的主要目的是阐述代码要做什么，以及是如何做的。
# 在开发项目期间，你对各个部分如何协同工作了如指掌，但是一段时间过后，你可能会忘记一些细节。
# 通过编写注释以清晰的自然语言对解决方案进行概述，可以节省很多时间。
# 要成为专业程序员或与其他程序员合作，就必须编写有意义的注释。当前，大多数软件是合作编写而成的。
# 程序员最值得养成的习惯之一就是，在代码中编写清晰、简洁的注释。
# 如果不确定是否要编写注释，就问问自己：在找到合理的解决方案之前，考虑了多个解决方案吗？
# 如果答案是肯定的，就编写注释，对你的解决方案进行说明吧。
# 相比以后再回头添加注释，删除多余的注释要容易得多。


# #是python官方定义的注释方式。
# ''' '''或者""" """可以用来注释多行内容。
# 但是要注意，#的注释会完全被python解释器忽略，而''' '''或者""" """会被当作字符串处理。
# 这意味着会在内存创建字符串对象，然后发现这个字符串对象没有被使用，垃圾回收机制会将其回收。
# 所以，''' '''或者""" """注释多行内容时，最好将其放在函数或类的开头。
# 这样可以作为文档字符串（docstring），供其他人查看函数或类的用途和功能。
# 当三引号字符串放在函数/类的开头时，解释器创建一个字符串对象。
# 发现它处于特殊位置，于是不会丢弃。而是将这个字符串对象赋值给那个函数或类的内置 __doc__ 属性。
# 这是python社区的最佳实践。
