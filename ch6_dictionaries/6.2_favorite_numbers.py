# 6-2. Favorite Numbers:
# Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary.
# Print each person’s name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {"Bob": 88, "Alice": 66, "John": 0, "Tom": 3012, "Jae": 996}
for person in favorite_numbers:
    print(f"The favorite number of {person} is {favorite_numbers[person]}")
