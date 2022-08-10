
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 1)
f_x = x ** 2

print('hello world')

x_new = 10
derivative = []
y = []

learning_rate = 0.1


for i in range(100):
    old_value = x_new
    derivative.append(old_value - learning_rate * 2 * old_value)

    x_new = old_value - learning_rate * 2 * old_value
    y.append(x_new ** 2)

plt.plot(x, f_x)
plt.scatter(derivative,y)
plt.show()