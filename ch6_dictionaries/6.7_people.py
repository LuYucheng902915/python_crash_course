# 6-7. People:
# Start with the program you wrote for Exercise 6-1 (page 98).
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know about each person.

person_0 = {"first name": "Lu", "last name": "Yucheng", "age": 26, "city": "Hangzhou"}
person_1 = {"first name": "Dong", "last name": "Jiajie", "age": 26, "city": "Hangzhou"}
person_2 = {"first name": "Yuan", "last name": "Zhiting", "age": 26, "city": "Hangzhou"}

people = [person_0, person_1, person_2]
for person in people:
    for attribute, value in person.items():
        print(f"The {attribute} of the person is {value}")
