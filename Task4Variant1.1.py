a = [1, 2, 3, 4, 3, 2, 3, 3, 2]
A = []
for x in a:
    if a.count(x)>2:
        a.remove(x)
print(a)
