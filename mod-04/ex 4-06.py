import random

n = input('How many numbers to generate: ')
i = 0
nn = 0

while i <= int(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        nn +=1
    i += 1
pi = 4 * nn / int(n)
print(f"The approximate value of pi is: {pi}")