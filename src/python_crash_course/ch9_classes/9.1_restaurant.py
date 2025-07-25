# 9-1. Restaurant:
# Make a class called Restaurant.
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#  Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"The cuisine type of the restaurant is {self.type}")

    def open_restaurant(self):
        print("The restaurant is open.")


restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
