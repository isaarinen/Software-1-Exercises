number = int(input('Enter a number: '))
prime = 0
if 4 > number > 0:
    print('The number is a prime.')
    prime = 1
elif number < 1:
    print('The number is less than one and cannot be prime.')
else:
    for i in range(4, number - 1):
        if number % i ==0:
            print('The number is not a prime.')
            prime = 1
            break


if prime == 0:
    print(f"{number} is a prime number.")