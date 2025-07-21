# 8-12. Sandwiches:
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered.
# Call the function three times, using a different number of arguments each time.


def make_sandwiches(*items):
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"  ...ading {item} to your sandwich.")
    print("Your sandwich is ready!")


make_sandwiches("roast beef", "cheddar cheese", "lettuce", "honey dijon")
make_sandwiches("turkey", "apple slices", "honey mustard")
make_sandwiches("peanut butter", "strawberry jam")
