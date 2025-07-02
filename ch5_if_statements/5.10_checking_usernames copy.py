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
