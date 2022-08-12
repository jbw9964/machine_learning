
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def function_return(w1, w2) : 
    return 3*(w1 - 2)**2 + 2*(w2 - 3)**2 + 3

w1 = np.linspace(0, 10)
w2 = np.linspace(0, 10)

W1, W2 = np.meshgrid(w1, w2)
E = function_return(W1, W2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

w1_i = 8
w2_i = 10

learning_rate = 0.1

def grad_w1(w1) : 
    return 6 * (w1 - 2)
def grad_w2(w2) : 
    return 2 * (w2 - 3)

learn_w1 = [w1_i]
learn_w2 = [w2_i]
learn_E = [function_return(w1_i, w2_i)]

for i in range(10) : 

    # w1_new, w2_new = (w1_i, w2_i) - learning_rate * (grad_w1(w1_i), grad_w2(w2_i))

    w1_new = w1_i - learning_rate * grad_w1(w1_i)
    w2_new = w2_i - learning_rate * grad_w2(w2_i)
    
    learn_w1.append(w1_new)
    learn_w2.append(w2_new)
    learn_E.append(function_return(w1_new, w2_new))

    w1_i, w2_i = w1_new, w2_new

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(W1, W2, E, alpha=0.5)
ax.plot(learn_w1, learn_w2, learn_E, 'o')
ax.plot(learn_w1.pop(), learn_w2.pop(), learn_E.pop(), '^')
# plt.xlim(0, 4)
# plt.ylim(1, 5)
plt.show()