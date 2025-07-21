# 3-7. Shrinking Guest List:
# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6.
# Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list.
# Each time you pop a name from your list, print a essage to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    message = f"‌I'd like to invite {name} to dinner"
    print(message)

guest_cant_make_it = "David"
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")
index_of_absent_guest = names.index(guest_cant_make_it)
names[index_of_absent_guest] = "Bobby"

for name in names:
    message = f"I'd like to invite {name} to dinner"
    print(message)

print("\nI found a bigger table, so I can invite more guests!\n")
names.insert(0, "Frank")
names.insert(2, "Grace")
names.append("Hannah")
for name in names:
    message = f"I'd like to invite {name} to dinner"
    print(message)

print("\nI can only invite two people to dinner.\n")
while len(names) > 2:
    removed_guest = names.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

for name in names:
    message = f"‌{name}, you're still invited to dinner."
    print(message)

print(f"Current guest list: {names}")

# Clear the list of names
names.clear()
print("\nThe guest list is now empty.")
print(f"Current guest list: {names}")
