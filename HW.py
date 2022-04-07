import Plate_list
def func1 (var=input("Input number ")):
    if len(var) == 8:
        return var[0:2], int(var[2]), int(var[3]), int(var[4]), int(var[5]), var[6:8]
    else:
        return input('Input correct 8 simbols of the number')
    func1(var)
print(func1())
def func2(var_1 = int(var[2:6])):
    return sum(map(int, str(var_1)))


func2(var_1)
print(func2())
