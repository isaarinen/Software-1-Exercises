import random

dice = int(input('How many dice do you want to roll? '))
n = 0

for i in range(0, dice):
    n += random.randint(1, 6)
print('The sum of the dice rolls:', n)