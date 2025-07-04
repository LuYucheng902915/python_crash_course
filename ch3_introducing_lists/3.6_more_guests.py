# 3-6. More Guests:
# You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    message = f"I'd like to invite {name} to dinner"
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
