# 7-3. Multiples of Ten:
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number_input = input("Please enter a number: ")
number = int(number_input)

if number % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("The number is not a multiple of 10.")
