from random import random

M = 5
N = 3
A = []
for i in range(N):
    B = []
    for j in range(M):
        B.append(int(random() * 11))
        print("%3d" % B[j], end='')
    A.append(B)
    print()

for i in range(M):
    print(" --", end='')
print()
max_sum = 0
col = 0
for i in range(M):
    s = 0
    for j in range(N):
        s += A[j][i]
    print("%3d" % s, end='')
    if s > max_sum:
        max_sum = s
        col = i
print()
print(col + 1)
