# 5-1. Conditional Tests:
# Write a series of conditional tests.
# Print a statement describing each test and your prediction for the results of each test.
# Your code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

# Variables for testing
car = "subaru"
animal = "cat"
year = 2025
temperature = 98.6

print("--- 5 Tests Evaluating to True ---")

# Test 1: String Equality
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

# Test 2: String Inequality
print("\nIs animal != 'dog'? I predict True.")
print(animal != "dog")

# Test 3: Numerical Equality
print("\nIs year == 2025? I predict True.")
print(year == 2025)

# Test 4: Greater Than
print("\nIs temperature > 90? I predict True.")
print(temperature > 90)

# Test 5: Less Than or Equal To
print("\nIs car length <= 6? I predict True.")
print(len(car) <= 6)

print("\n--- 5 Tests Evaluating to False ---")

# Test 6: String Equality
print("Is car == 'toyota'? I predict False.")
print(car == "toyota")

# Test 7: Numerical Inequality
print("\nIs year != 2025? I predict False.")
print(year != 2025)

# Test 8: Less Than
print("\nIs temperature < 98? I predict False.")
print(temperature < 98)

# Test 9: Greater Than or Equal To
print("\nIs year >= 2026? I predict False.")
print(year >= 2026)

# Test 10: String Inequality
print("\nIs animal != 'cat'? I predict False.")
print(animal != "cat")
