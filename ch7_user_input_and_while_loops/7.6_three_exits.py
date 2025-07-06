#  7-6. Three Exits:
# Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nPlease enter a series of pizza toppings."
prompt += "\nEnter 'quit' when you're finished: "
active = True

while active:
    topping = input(prompt)

    if topping != "quit":
        print(f"I'll add the {topping} to your pizza!")
    else:
        active = False


prompt = "\nPlease enter your age, and I'll tell you the cost of your movie ticket."
prompt += "\nEnter 'quit' to finish the program. "
age_input = ""

while age_input != "quit":
    age_input = input(prompt)
    if age_input != "quit":
        age = int(age_input)
        if age < 3:
            print("The cost of your ticket is 0.")
        elif age <= 12:
            print("The cost of your ticket is $10.")
        else:
            print("The cost of your ticket is $15.")


prompt = "\nPlease enter your age, and I'll tell you the cost of your movie ticket."
prompt += "\nEnter 'quit' to finish the program. "

while True:
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
        break
