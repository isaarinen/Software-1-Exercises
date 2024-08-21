import random

three_dig_1 = random.randint(0, 9)
three_dig_2 = random.randint(0, 9)
three_dig_3 = random.randint(0, 9)
four_dig_1 = random.randint(1, 6)
four_dig_2 = random.randint(1, 6)
four_dig_3 = random.randint(1, 6)
four_dig_4 = random.randint(1, 6)


print('3 digit code:', f"{three_dig_1}" + f"{three_dig_2}" + f"{three_dig_3}")
print('4 digit code:', f"{four_dig_1}" + f"{four_dig_2}" + f"{four_dig_3}" + f"{four_dig_4}")