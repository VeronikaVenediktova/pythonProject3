import time

def summary(x):
    sum = 0
    for all in range(0, x+1):
        sum+= all
    return sum
time_start = time.time()
a = summary(100_000_000)
t2 = time.time()
print(t2 - time_start)
def summary2(x):
    dlina = x
    visota = x+1
    sum = dlina*visota/2
    return sum
print(summary2(99))
print(summary(99))
time_start = time.time()
a = summary2(100_000_000)
t2 = time.time()



