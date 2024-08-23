def int_sum(integers):
    ints = 0
    for i in integers:
        ints += i
    return ints

int_list = [6, 9, 15, 7, 20]
print(int_sum(int_list))