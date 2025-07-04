# 2-7. Stripping Names:
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

famous_person = "\n\tAlbert Einstein\t\n\n"
print(famous_person)
print("Divider" + "-" * 20)
print(famous_person.strip())
print("Divider" + "-" * 20)
print(famous_person.lstrip())
print("Divider" + "-" * 20)
print(famous_person.rstrip())
print("Divider" + "-" * 20)
