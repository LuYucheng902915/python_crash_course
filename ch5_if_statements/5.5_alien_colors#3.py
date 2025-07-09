# 5-5. Alien Colors #3:
# Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed for the appropriate color alien.

# Green alien version
print("Green alien version:")
alien_color = "green"

if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# Yellow alien version
print("\nYellow alien version:")
alien_color = "yellow"

if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# Red alien version
print("\nRed alien version:")
alien_color = "red"

if alien_color == "green":
    print("You earned 5 points.")
elif alien_color == "yellow":
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

print("\n---\n")
