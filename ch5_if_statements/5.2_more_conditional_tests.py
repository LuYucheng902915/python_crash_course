# 5-2. More Conditional Tests:
# You don’t have to limit the number of tests you create to 10.
# If you want to try more comparisons, write more tests and add them to conditional_tests.py.
# Have at least one True and one False result for each of the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

print("\n--- More Conditional Tests ---")

# Variables for Part 2
topping = "Mushroom"
alien_color = "green"
user_age = 25
banned_users = ["andrew", "carolina", "david"]

# Tests for equality and inequality with strings
print("\nIs topping == 'Mushroom'? I predict True.")
print(topping == "Mushroom")

print("\nIs topping != 'Mushroom'? I predict False.")
print(topping != "Mushroom")

# Tests using the lower() method
print("\nIs topping.lower() == 'mushroom'? I predict True.")
print(topping.lower() == "mushroom")

print("\nIs topping.lower() == 'Mushroom'? I predict False.")
print(topping.lower() == "Mushroom")

# Numerical tests
print("\nIs user_age == 25? I predict True.")
print(user_age == 25)

print("\nIs user_age != 30? I predict True.")
print(user_age != 30)

print("\nIs user_age > 18? I predict True.")
print(user_age > 18)

print("\nIs user_age < 20? I predict False.")
print(user_age < 20)

print("\nIs user_age >= 25? I predict True.")
print(user_age >= 25)

print("\nIs user_age <= 20? I predict False.")
print(user_age <= 20)

# Tests using the and keyword and the or keyword
print("\nIs user_age > 20 and alien_color == 'green'? I predict True.")
print(user_age > 20 and alien_color == "green")

print("\nIs user_age < 20 and alien_color == 'green'? I predict False.")
print(user_age < 20 and alien_color == "green")

print("\nIs user_age < 20 or alien_color == 'green'? I predict True.")
print(user_age < 20 or alien_color == "green")

print("\nIs user_age < 20 or alien_color == 'red'? I predict False.")
print(user_age < 20 or alien_color == "red")

# Test whether an item is in a list
print("\nIs 'marie' in banned_users? I predict False.")
print("marie" in banned_users)

print("\nIs 'david' in banned_users? I predict True.")
print("david" in banned_users)

# Test whether an item is not in a list
print("\nIs 'john' not in banned_users? I predict True.")
print("john" not in banned_users)

print("\nIs 'andrew' not in banned_users? I predict False.")
print("andrew" not in banned_users)
