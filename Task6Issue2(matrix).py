import random
n=int(input('Введите кол-во строк и столбцов матрицы: '))
h=('')
matrix=[[random.randrange(10) for i in range(n)] for j in range(n)]
for elem in matrix:
    print(elem)
for k in range(0,n-1):
    for l in range(k+1,n):
        if matrix[k][l]!=matrix[l][k]:
            h=('False')
            break
if h!=('False'):
    print('Симметричная матрица')
else:
    print('Обычная матрица')