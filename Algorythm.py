import time

def summary(x):
    sum = 0
    for all in range(0, x+1):
        sum+= all
    return sum
t1 = time.time()
a = summary(100_000_000)
t2 = time.time()
print(t2-t1)
def summary2(x):
    dlina = x
    visota = x+1
    sum = dlina*visota/2
    return sum
print(summary2(99))
print(summary(99))
t1 = time.time()
a = summary2(100_000_000)
t2 = time.time()



