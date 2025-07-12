# 6-10. Favorite Numbers:
# Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    "bob": [88, 7, 42],
    "alice": [66],
    "john": [0, 1, 2, 3],
    "tom": [3012, 100],
    "jae": [996, 777, 123],
}

print("--- Favorite Numbers ---")
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    # Use join to print the list nicely
    print(f"\t{', '.join(map(str, numbers))}")
