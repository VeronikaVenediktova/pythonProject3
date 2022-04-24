l = [1, 2, 'a', 'b']


def filter_list(l):
    global l1
    l1 = []
    for x in l:
        if type(x) == int:
            l1.append(x)
    return l1
print(filter_list(l))
