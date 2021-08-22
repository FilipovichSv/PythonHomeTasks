import random

a = [0]
n = int(input(5))
A = []
for i in range(n):
    a = random.randint(0, 99)
    A.append(a)
    list.remove(a)
