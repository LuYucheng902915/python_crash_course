menu = ("fish", "beef", "fruits", "chicken", "pork")
for food in menu:
    print(food)

# menu[0] = "mutton"
# TypeError: 'tuple' object does not support item assignment

menu = ("fish", "mutton", "fruits", "duck", "pork")
for food in menu:
    print(food)
