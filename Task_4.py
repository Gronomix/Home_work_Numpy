'''Решить задачу поиска наименьших квадратов для линейного матричного уравнения.'''

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio


x = np.arange(10)
y = 2*x + 4 + 2*np.random.randn(10)
print(x)
print(y)

plt.scatter(x, y)
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
pio.renderers.default = 'png'
plt.plot(x, m*x + c, 'r')
plt.show()




