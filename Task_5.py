'''Будет CSV файл с набором измерений. Нужно рассчитать дисперсию, среднеквадратичное отклонение,
отобразить гистограмму и решить задачу поиска наименьших квадратов.
Нужно реализовать программу, которая принимает текстовый файл (в файле есть все данные для заданий 1-4) и
записывает ответы для каждого задания в единый файл и сохраняет его на компьютере.
Для задания 5 все то же самое только принимает CSV и возвращает .txt файл + изображение
с гистограммой + изображение с решением задачи поиска наименьших квадратов.'''

import numpy as np
import matplotlib.pyplot as plt
import csv
import plotly.io as pio
import pandas as pd

df = pd.read_csv('data_xy.csv', usecols=['X','Y'])
print(df)
print(df.describe())
data_x = df['X'].copy()
print(data_x)

data_y = df['Y'].copy()

print(data_y)
x = np.array(data_x)
y = np.array(data_y)
print(x)
print(y)

plt.scatter(x, y, s=6, c='red')
plt.show()

a = np.vstack(x)
b = np.vstack(y)
print(a)
m, c = np.linalg.lstsq(a, b, rcond=None)[0]
plt.plot(a, m * a + c, 'r')
plt.show()




