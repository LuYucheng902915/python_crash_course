# 5-9. No Users:
# Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.

users = ["jaden", "sarah", "admin"]
if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("\n")

# Version with no users
users = []
if users:
    for user in users:
        # This block will not run
        pass
else:
    print("We need to find some users!")
