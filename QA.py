from random import randint

data = [75, 70, 43, 71, 22, 52, 74, 12, 69, 26, 38, 37, 1, 57, 6, 80, 32, 2, 66, 15, 58, 33, 1, 3]
data_updated = []
n = data[0]
while len(data) != 0:
    n = d bb ata[0]
    m1 = max(data)
    data.remove(m1)
    data_updated.append(m1)
    print(data, data_updated, f'{n=}')
    for position, i in enumerate(data):
        if i >= n:
            n = i
            data_updated.insert(-1, data.pop(position))
print(data_updated)
