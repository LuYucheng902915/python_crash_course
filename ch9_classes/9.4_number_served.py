# 9-4. Number Served:
# Start with your program from Exercise 9-1 (page 162).
# Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.


class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}")
        print(f"The cuisine type of the restaurant is {self.type}")

    def open_restaurant(self):
        print("The restaurant is open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(20)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)
