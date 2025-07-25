# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number.
# Use json.dumps() to store this number in a file.
# Write a separate program that reads in this value and prints the message “I know your favorite number! It’s _____.”

import json
from pathlib import Path

number = input("What's your favourite number? ")

path = Path("favorite_number.json")
contents = json.dumps(number)
path.write_text(number)
print("Thanks, I'll remember that number.")

contents = path.read_text()
number = json.loads(contents)
print(f"I know your favorite number! It's {number}.")
