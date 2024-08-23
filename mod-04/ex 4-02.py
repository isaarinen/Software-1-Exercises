neg_test = 1
while bool(neg_test):
    inches = input('Enter inches: ')
    if int(inches) < 0:
        neg_test = 0
        break
    cms = int(inches) * 2.54
    print(f"{inches} inches is: {cms:.2f} centimeters")