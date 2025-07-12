# 6-8. Pets:
# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets.
# Next, loop through your list and as you do, print everything you know about each pet.

pet_1 = {"kind": "dog", "owner": "sarah"}
pet_2 = {"kind": "cat", "owner": "john"}
pet_3 = {"kind": "hamster", "owner": "emily"}
pet_4 = {"kind": "parrot", "owner": "david"}

# Store the dictionaries in a list called pets
pets = [pet_1, pet_2, pet_3, pet_4]

# Loop through the list and print information about each pet
print("--- Pet Information ---")
for pet in pets:
    print(f"\nHere is what I know about {pet['owner'].title()}'s pet:")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value.title()}")
