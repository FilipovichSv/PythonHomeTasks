from math import copysign

lst = list(map(int, "9 -4 3 56 -4 8".split()))
count = -1
sig = 1
for i in lst:
    if copysign(1, i) != sig:
        count += 1
        sig = -sig
    print(count)
