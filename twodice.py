import random

def two_dice():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    if roll1 + roll2 >= 6 and roll1 + roll2 <= 8:
        return ("win")
    else:
        return ("lose")

print(two_dice())