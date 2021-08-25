a = [1,2,3,4]
point = 5
for a[0] in a:
    for a[1] in a:
        x=(a[0] + a[1])
        if x == point:
            print(x)
        else:
            print('not found')
for a[1] in a:
    for a[2] in a:
        x=(a[1] + a[2])
        if x == point:
            print(x)
        else:
            print('not found')
for a[2] in a:
    for a[3] in a:
        x=(a[2] + a[3])
        if x == point:
            print(x)
        else:
            print('not found')