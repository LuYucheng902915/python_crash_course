# 9-2. Three Restaurants:
# Start with your class from Exercise 9-1.
# Create three different instances from the class, and call describe_restaurant() for each instance.


class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"The cuisine type of the restaurant is {self.type}")

    def open_restaurant(self):
        print("The restaurant is open.")


mean_queen = Restaurant("the mean queen", "pizza")
mean_queen.describe_restaurant()

ludvigs = Restaurant("ludvig's bistro", "seafood")
ludvigs.describe_restaurant()

mango_thai = Restaurant("mango thai", "thai food")
mango_thai.describe_restaurant()
