a = int(input("Длина:  "))
b = int(input("Ширина: "))

area = a * b

def to_quadrats(area):
    if area == 0:
        raise StopIteration
    while(area):
        for i in range(area, 0, -1):
            if i * i <= area:
                area -= i * i
                yield i
                break
        to_quadrats(area)

result = list(to_quadrats(area))
print(result)
