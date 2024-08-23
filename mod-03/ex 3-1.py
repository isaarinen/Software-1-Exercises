length = input('How many centimeters is the zander? ')
if int(length) < 42:
    limit = 42 - int(length)
    print(f"The fish is {limit} centimeters below the size limit, you must release it back into the lake.")