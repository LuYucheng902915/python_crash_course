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
