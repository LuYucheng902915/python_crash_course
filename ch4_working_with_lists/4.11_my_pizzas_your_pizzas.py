pizzas = ["Neapolitan Pizza", "Margherita Pizza", "Chicago Pizza"]

for pizza in pizzas:
    message = f"I like {pizza}"
    print(message)

print("I really love pizza!")

friend_pizzas = pizzas[:]
friend_pizzas.append("Quattro Stagioni Pizza")
print("My favorite pizzas are:")
for pizza in pizzas:
    message = f"I like {pizza}"
    print(message)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    message = f"My friend like {pizza}"
    print(message)
