'''Решить задачу поиска наименьших квадратов для линейного матричного уравнения.'''

import numpy as np

A = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 0]]
B = [1, 1, 1, 1, 1]
W = [1, 2, 3, 4, 5]

W = np.sqrt(np.diag(W))

Aw = np.dot(W, A)
Bw = np.dot(B, W)

X = np.linalg.lstsq(Aw, Bw, rcond=-1)
print(X[0])