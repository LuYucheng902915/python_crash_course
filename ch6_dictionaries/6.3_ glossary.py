# 6-3. Glossary:
# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

# Create a dictionary to store programming words and their meanings.
glossary = {
    "variable": "A container for storing a value.",
    "list": "A collection of items in a particular order. Lists are mutable.",
    "tuple": "A collection of items that cannot change. Tuples are immutable.",
    "f-string": "A string literal that lets you include the value of Python expressions inside the string.",
    "dictionary": "A collection of key-value pairs.",
    "conditional test": "An expression that can be evaluated as either True or False, used in an if statement.",
}

# Loop through the dictionary and print each word and its meaning.
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")

# glossary.items()本身返回的是一个特殊的、可迭代的“字典视图对象”（dict_items）。
# 可以理解为返回一个列表，您可以把它想象成一个列表，其中每个元素都是一个元组（tuple），元组的第一个元素是字典的键（key），第二个元素是对应的值（value）。
# 但并不在内存中真的生成这样一个列表。
"""
[
    ('variable', 'A container for storing a value.'),
    ('list', 'A collection of items in a particular order...'),
    ('tuple', 'A collection of items that cannot change...'),
    ...
]
"""
# 类似返回上面的格式
# 当用 for 循环去遍历这个视图对象时，它每一次循环产出的元素，是一个包含(键, 值)的小元组。
# 而 for key, value in ... 这个语法正是利用了“元组解包”的特性，将每个小元组里的两个元素，自动赋给了 key 和 value 两个变量。
# 在每次循环时，Python会非常智能地将每个元组 (key, value) 自动“解包”，把元组的第一个元素赋给变量 key，第二个元素赋给变量 value。
# 元组解包 (Tuple Unpacking) 是一种将元组中的多个元素，一次性地、分别赋值给多个变量的简洁语法。
# 关键规则是，等号左边变量的数量必须和右边元组中元素的数量完全一致。
for word in glossary:
    print(f"{word.title()}:\n\t{glossary[word]}\n")

# 这种写法，每次循环从字典中取出一个键 word。再用这个键 word，通过 glossary[word] 返回字典里再次进行一次查找，以获取对应的值。
# .items() 写法 (for key, value in dict.items()): 在循环的每一步，只执行了一次操作。
# .items() 方法在迭代时，会将键和对应的值一次性成对地取出来，直接分别赋给 key 和 value。它避免了第二次查找。
# 但如果字典有成千上万个条目，使用 .items() 会因为减少了一半的查找操作而变得明显更高效。
