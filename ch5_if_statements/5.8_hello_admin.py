# 5-8. Hello Admin
usernames = ["jaden", "sarah", "admin", "eric", "chloe"]

for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
