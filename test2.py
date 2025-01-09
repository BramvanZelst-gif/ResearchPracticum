import numpy as np
import matplotlib.pyplot as plt

n = 0
y = []
for i in range(0,20):
    y_waarde = 40 * np.sin(2 * np.pi * n / 0.006) + 80
    y.append(y_waarde)
    n = n + 0.001

x = []
for k in range(0,20):

    x.append(k)

y = []
for i in range(0,20):
    y_waarde = np.sin(i)
    y.append(y_waarde)
    n = n + 0.001

plt.plot(x, y)
plt.show()