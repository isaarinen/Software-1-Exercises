year = input('Enter the year: ')
if int(year) >= 100:
    if int(year) % 4 == 0:
        if int(year) % 100 == 0 and int(year) % 400 == 0:
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is not a leap year.")
else:
    if int(year) % 4 == 0:
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")