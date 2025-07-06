# 7-4. Pizza Toppings:
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

prompt = "\nPlease enter a series of pizza toppings."
prompt += "\nEnter 'quit' when you're finished: "
topping = ""

while topping != "quit":
    topping = input(prompt)

    if topping != "quit":
        print(f"I'll add the {topping} to your pizza!")
