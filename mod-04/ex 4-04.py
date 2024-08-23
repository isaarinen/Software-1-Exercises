import random

number = random.randint(1, 10)
game = 1
while bool(game):
    guess = input('Guess the number:')
    if int(guess) == number:
        print('Correct')
        game = 0
    elif int(guess) > number:
        print('Too high')
    else:
        print('Too low')