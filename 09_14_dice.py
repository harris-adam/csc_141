from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

six_sided_die = Die()
for _ in range(10):
    print(six_sided_die.roll_die())

ten_sided_die = Die(10)
for _ in range(10):
    print(ten_sided_die.roll_die())

twenty_sided_die = Die(20)
for _ in range(10):
    print(twenty_sided_die.roll_die())