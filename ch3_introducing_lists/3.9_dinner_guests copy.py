# 3-9. Dinner Guests:
# Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), use len() to print a message indicating the number of people you’re inviting to dinner.

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    message = f"‌I'd like to invite {name} to dinner"
    print(message)

numbers = len(names)
message = f"I'd like to invite {numbers} guests to dinner"
print(message)
