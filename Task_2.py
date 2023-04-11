'''Будет СЛАУ которую нужно решить методом Гаусса/Крамера.'''

import numpy as np

def kramer(A, b):
    n = len(A)
    detA = det(A)
    x = []
    for i in range(n):
        B = A.copy()
        for j in range(n):
            B[j][i] = b[j]
        detB = det(B)
        x.append(detB / detA)

    return x

def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 1:
        return A[0][0]
    else:
        sign = 1
        detA = 0
        for j in range(n):
            B = []
            for i in range(1, n):
                row = []
                for k in range(n):
                    if k != j:
                        row.append(A[i][k])
                B.append(row)
            detA += sign * A[0][j] * det(B)
            sign *= -1
        return detA

A = [[2, 3, -1],
     [4, -1, 3],
     [1, 2, -1]]
b = [9, 8, 3]

x = kramer(A, b)

print(f"x1 = {x[0]}")
print(f"x2 = {x[1]}")
print(f"x3 = {x[2]}")

print(f'Второй способ через Numpay при таких же данных A = {A} и b =  {b} ')



a1 = [[2, 3, -1], [4, -1, 3], [1, 2, -1]]

b1 = [9, 8, 3]

def Kram(A,B):

    m = len(A)
    op = np.linalg.det(A)
    print(op)
    r = list()
    for i in range(m):
        VM = np.copy(A)
        VM[:,i] = B
        r.append(np.linalg.det(VM)/op)
        return r

X3 = Kram(a1,b1)
print(X3)



