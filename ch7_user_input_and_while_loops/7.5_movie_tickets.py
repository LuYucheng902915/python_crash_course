# 7-5. Movie Tickets:
# A movie theater charges different ticket prices depending on a person’s age.
# If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prompt = "\nPlease enter your age, and I'll tell you the cost of your movie ticket."
prompt += "\nEnter 'quit' to finish the program. "

active = True

while active:
    age_input = input(prompt)
    if age_input != "quit":
        age = int(age_input)
        if age < 3:
            print("The cost of your ticket is 0.")
        elif age <= 12:
            print("The cost of your ticket is $10.")
        else:
            print("The cost of your ticket is $15.")
    else:
        active = False
