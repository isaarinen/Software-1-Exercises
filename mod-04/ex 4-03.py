first_guess = input('Enter a number: ')
if first_guess == '':
    print('The first guess was empty, game over.')
else:
    highest_guess = first_guess
    lowest_guess = first_guess
    while True:
        guess = input('Enter a number: ')
        if guess == '':
            print(f"Your highest guess was {highest_guess}")
            print(f"Your lowest guess was {lowest_guess}")
            break
        elif int(guess) > int(highest_guess):
            highest_guess = guess
        elif int(guess) < int(lowest_guess):
            lowest_guess = guess