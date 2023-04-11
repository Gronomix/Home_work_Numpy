'''Решить линейное тензорное уравнение'''

import numpy as np
from numpy import linalg as LA

a = np.random.randint(0, 10, size = (3, 2, 2, 3))
print(a)

b = np.random.randint(0, 10, size = (3, 2))
print(b)

x = LA.tensorsolve(a, b)
x_2 = LA.tensorsolve(a, b, axes=(0, 1))
print(x)
print(f'Переопределяем элементы еунзора {x_2}')

result = np.tensordot(a, x)
print(result)

result2 = np.allclose(np.tensordot(a, x), b)

print(result2)

