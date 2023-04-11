'''Будет текстовый файл с числами которые нужно использовать для создания массива.'''

import numpy as np

arr = 'genfromtxt_example.txt'
arr2 = 'new.txt'

arr_1 = np.array(np.genfromtxt(arr))
print(arr_1)
arr_2 = np.array(np.loadtxt(arr))
print(arr_2)
arr_3 = np.array(np.genfromtxt(arr2))
print(arr_3)

data = np.loadtxt("new.txt", delimiter='\t', dtype=np.int)
print(data)
