def converter(gallons):
    litres = gallons * 3.785
    return litres

while True:
    n = int(input('Enter the volume in gallons: '))
    if n < 0:
        break
    litre = converter(n)
    print(f"{n} gallons is {litre} litres")