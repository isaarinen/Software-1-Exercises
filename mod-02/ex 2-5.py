tals = int(input('Enter talents: '))
pnds = int(input('Enter pounds: '))
lot = int(input('Enter lots: '))
a = tals * 20 + pnds
b = pnds * 32 + lot
c = b * 13.3
kgs = int(c) / 1000
grams = c - int(kgs) * 1000
print('The weight in modern units:\n' + f"{int(kgs)}" , 'kilograms and', f"{grams:.2f}", 'grams.')