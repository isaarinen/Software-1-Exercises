import random

def dice_roll(sides):
    roll_number = random.randint(1, sides)
    return roll_number

n = int(input('Enter the number of sides on the dice: '))

while True:
    roll = dice_roll(n)
    if roll == n:
        print(roll)
        break
    print(roll)