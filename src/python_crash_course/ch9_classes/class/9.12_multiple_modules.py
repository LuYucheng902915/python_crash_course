# 9-12. Multiple Modules:
# Store the User class in one module, and store the Privileges and Admin classes in a separate module.
# In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

from admin import Admin

eric = Admin("eric", "matthes", "e_matthes", "e_matthes@example.com", "alaska")
eric.describe_user()

eric_privileges = [
    "can reset passwords",
    "can moderate discussions",
    "can suspend accounts",
]
eric.privileges.privileges = eric_privileges

print(f"\nThe admin {eric.username} has these privileges: ")
eric.privileges.show_privileges()
