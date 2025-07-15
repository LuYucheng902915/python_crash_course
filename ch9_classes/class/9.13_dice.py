# 9-13. Dice:
# Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die.
# Roll each die 10 times.

from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


sided6_die = Die()
for _ in range(10):
    sided6_die.roll_die()


sided10_die = Die(10)
for _ in range(10):
    sided10_die.roll_die()


sided20_die = Die(20)
for _ in range(10):
    sided20_die.roll_die()
