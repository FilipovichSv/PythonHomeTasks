from random import randint

A = []
a = 1
n = int(input(5))
while a <= n:
    A.append(randint(0, 99))
    a += 1
print(A)
list.pop(a)

