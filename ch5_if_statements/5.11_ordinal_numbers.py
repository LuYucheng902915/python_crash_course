# 5-11. Ordinal Numbers:
# Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

numbers = [num for num in range(1, 10)]

for number in numbers:
    if number == 1:
        ordinal = "1st"
    elif number == 2:
        ordinal = "2nd"
    elif number == 3:
        ordinal = "3rd"
    else:
        ordinal = f"{number}th"

    print(ordinal)
