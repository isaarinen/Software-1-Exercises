def int_even(integers):
    even_ints = []
    for i in integers:
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints

int_list = [6, 9, 15, 7, 20, 2, 4, 8, 12, 11, 13, 2]

print(int_list)
print(int_even(int_list))