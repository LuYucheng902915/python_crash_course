# 使用 while 循环处理列表和字典。
# 我们每次都只处理了一项用户信息：获取用户的输入，再将输入打印出来或做出响应；循环再次运行时，获取另一个输入值并做出响应。
# 然而，要记录大量的用户和信息，需要在 while 循环中使用列表和字典。

# for 循环是一种遍历列表的有效方式，但不应该在 for 循环中修改列表，否则将导致 Python 难以跟踪其中的元素。
# 要在遍历列表的同时修改它，可使用 while 循环。
# 通过将 while 循环与列表和字典结合起来使用，可收集、存储并组织大量的输入，供以后查看和使用。

# 在列表之间移动元素。
# 首先，创建一个待验证用户列表和一个用于存储已验证用户的空列表。
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止，将每个经过验证的用户都移到已验证用户列表中。
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    # 显示所有的已验证用户。
    print(f"Verifying user: {current_user.title()}")
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# while 循环将不断地运行，直到列表 unconfirmed_users 变成空的。

# 使用 remove() 函数来删除列表中的特定值。这之所以可行，是因为要删除的值在列表中只出现了一次。
# 如果要删除列表中所有为特定值的元素，应该如下操作。
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)
# Python不断删除某个元素，直到发现它不在列表中，然后退出循环。

# 可以使用 while 循环提示用户输入任意多的信息。
# 使用用户输入填充字典。
# 下面创建一个调查程序，其中的循环在每次执行时都提示输入被调查者的名字和回答。
# 将收集到的数据存储在一个字典中，以便将回答与被调查者关联起来。
responses = {}
# 设置一个标志，指出调查是否继续。
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # 将回答存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False
    # 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
# 用户输入 no， while循环就结束。用户输入存储在字典中，最后用 for 循环显示。
