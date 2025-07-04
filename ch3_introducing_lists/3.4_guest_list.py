# 3-4. Guest List:
# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

names = ["alice", "bob", "charlie", "david", "eve"]
for name in names:
    message = f"I'd like to invite {name.title()} to dinner"
    print(message)
