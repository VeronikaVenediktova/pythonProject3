plates_list = ['HH9901CC', 'CA9150WC', 'BH7144WB', 'AI7665KU', 'AI8045DS', 'HH1233HH', 'AI1552MG', 'AI7232BO', 'AI9224SI', 'AI5813YC', 'CA7641NN',]
var = input("Input number ")
def func1(var):
    if len(var) != 8:
        print('Input correct 8 simbols of the number')
    else:
        return (var[0:2], int(var[2]), int(var[3]), int(var[4]), int(var[5]), var[6:8])
func1(var)
print(func1(var))
var_3 = int(var[2:6])
def func2(var_3):
    return sum(map(int, str(var_3)))
func2(var_3)
print(func2(var_3))