import math

def pizza_calc(diameter, price):
    area = math.pi/4 * diameter
    unit_price = area / price
    return unit_price

dia1 = int(input('Enter the diameter of the first pizza: '))
pri1 = int(input('Enter the price of the first pizza: '))
dia2 = int(input('Enter the diameter of the second pizza: '))
pri2 = int(input('Enter the price of the second pizza: '))

pizza1 = pizza_calc(dia1, pri1)
pizza2 = pizza_calc(dia2, pri2)

if pizza1 > pizza2:
    print('The first pizza is better value for money.')
else:
    print('The second pizza is better value for money.')