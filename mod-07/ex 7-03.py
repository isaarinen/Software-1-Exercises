airports = dict()

print('"fetch" to fetch an existing airport')
print('"new" to enter a new airport')
print('"quit" to exit the program')
while True:
    command = input('What do you want to do? ')
    if command == 'fetch':
        icao = input('Enter the ICAO code of the airport: ')
        print(airports[icao])
    if command == 'new':
        icao = input('Enter the ICAO code of the airport: ')
        name = input('Enter the name of the airport: ')
        airports[icao] = name
    if command == 'quit':
        break