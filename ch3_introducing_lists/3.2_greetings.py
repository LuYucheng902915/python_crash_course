# 3-2. Greetings:
# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person’s name.

names = ["alice", "bob", "charlie", "david", "eve"]
print(f"Hello, {names[0].title()}!")
print(f"Hello, {names[1].title()}!")
print(f"Hello, {names[2].title()}!")
print(f"Hello, {names[3].title()}!")
print(f"Hello, {names[4].title()}!")

for name in names:
    message = f"Hello, {name.title()}!"
    print(message)
