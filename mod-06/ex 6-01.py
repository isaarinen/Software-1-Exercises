import random

def dice_roll():
    roll_number = random.randint(1, 6)
    return roll_number

while True:
    roll = dice_roll()
    if roll == 6:
        print(roll)
        break
    print(roll)