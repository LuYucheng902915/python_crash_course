# 5-10. Checking Usernames:
# Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users.
# Make sure one or two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already been used.
# If it has, print a message that the person will need to enter a new username.
# If a username has not been used, print a message saying that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
# (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ["John", "eric", "sarah", "admin", "Mike"]
new_users = ["susan", "JOHN", "dave", "mike", "peter"]

# Create a case-insensitive copy of current_users
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(
            f"Sorry, the username '{new_user}' is already taken. Please enter a new username."
        )
    else:
        print(f"The username '{new_user}' is available.")


print("\n---\n")
