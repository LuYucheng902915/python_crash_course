# 6-1. Person:
# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.

person = {"first_name": "Lu", "last_name": "Yucheng", "age": 26, "city": "Hangzhou"}
for attribute in person:
    print(f"The {attribute} of the person is {person[attribute]}")

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])
