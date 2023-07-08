import random

class Dice:
    def roll(self):
        coord = (random.randint(1,6),random.randint(1,6))
        return coord


dice1 = Dice()
print(dice1.roll())
