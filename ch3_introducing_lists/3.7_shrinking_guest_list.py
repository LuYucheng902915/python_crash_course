names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    message = f"‌I'd like to invite {name} to dinner"
    print(message)

guest_cant_make_it = "David"
print(f"\nUnfortunately, {guest_cant_make_it} can't make it to the dinner.\n")
index_of_absent_guest = names.index(guest_cant_make_it)
names[index_of_absent_guest] = "Bobby"

for name in names:
    message = f"‌I'd like to invite {name} to dinner"
    print(message)

print("\nI found a bigger table, so I can invite more guests!\n")
names.insert(0, "Frank")
names.insert(2, "Grace")
names.append("Hannah")
for name in names:
    message = f"‌I'd like to invite {name} to dinner"
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
