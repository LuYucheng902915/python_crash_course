# 3-5. Changing Guest List:
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

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
