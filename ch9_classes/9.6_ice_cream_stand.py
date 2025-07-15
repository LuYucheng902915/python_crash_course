# 9-6. Ice Cream Stand:
# An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166).
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.


class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"The cuisine type of the restaurant is {self.type}")

    def open_restaurant(self):
        print("The restaurant is open.")


class IceCreamStand(Restaurant):
    def __init__(self, name, type="ice cream", flavors=[]):
        super().__init__(name, type)
        self.flavors = flavors

    def display_flavors(self):
        for flavor in self.flavors:
            print(f"{flavor.title()}")


big_one = IceCreamStand("The big one")
big_one.flavors = ["vanilla", "chocolate", "black cherry"]

big_one.describe_restaurant()
big_one.display_flavors()
