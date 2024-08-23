numbers = []

while True:
    number = input('Enter a number: ')
    if number != '':
        numbers.append(int(number))
    else:
        break
numbers.sort(reverse=True)
print(numbers[:5])