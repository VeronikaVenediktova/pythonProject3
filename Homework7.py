# import Plate_list
# var = input("Input number ")


def func1(var):
    if len(var) == 8:
        first_symbol = var[0:2]
        first_digit = int(var[2])
        second_digit = int(var[3])
        third_digit = int(var[4])
        four_digit = int(var[5])
        second_symbol = var[6:8]
        return (first_symbol, first_digit, second_digit, third_digit, four_digit, second_symbol)
    else:
        return False


def sum_count(result):
    sum: int = 0
    for count in result:
        if isinstance(count, int):
            sum += count
    return sum


# result = func1(var)
#
# if not(result):
#     print('Input correct 8 symbols of the number')
# else:
#     print(sum_count(result))

