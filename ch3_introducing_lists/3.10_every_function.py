names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]

print(names)
print("-" * 20)

for i in range(4):
    print(names[i], " ", names[i].title(), " ", names[i].upper(), " ", names[i].lower())
print("-" * 20)

for i in range(-1, -5, -1):
    message = "Top star: {names[i]}"
    print(message)
print("-" * 20)

message = f"My favorite singer is {names[1].title()}."
print(message)
print("-" * 20)

for i in range(4):
    names[i] = names[i].title()
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
names[1] = "Anne Hathaway"
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
names.append("Anne Hathaway")
print(names)
print("-" * 20)

names_copy = []
for name in names:
    names_copy.append(name)
print(names_copy)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
names.insert(2, "Anne Hathaway")
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
name = names[2]
print(names)
print(name)
index_of_name = names.index(name)
print(index_of_name)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
print(len(names))
del names[-1]
print(names)
print(len(names))
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
print(len(names))
deleted_name = names.pop(1)  # 如果不传参数，默认删除最后一个元素
print(deleted_name)
print(names)
print(len(names))
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
print(len(names))
deleted_name = "Tom cruise"
print(id(names[0]))
print(id(deleted_name))
names.remove(deleted_name)
print(deleted_name)
print(id(deleted_name))
print(names)
print(len(names))
deleted_name = names[1]
print(id(names[1]))
print(id(deleted_name))
names.remove(deleted_name)
print(deleted_name)
print(id(deleted_name))
print(names)
print(len(names))
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
while len(names) != 0:
    deleted_name = names.pop()
    print(f"Name {deleted_name} deleted!")
print(len(names))
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
names.clear()
print(len(names))
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
names.sort()
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
names.sort(reverse=True)
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
names.reverse()
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
print(sorted(names))
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(names)
print(sorted(names, reverse=True))
print(names)
print("-" * 20)

names = ["Tom cruise", "Taylor swift", "Chris evans", "Jennifer lawrence"]
print(len(names))
