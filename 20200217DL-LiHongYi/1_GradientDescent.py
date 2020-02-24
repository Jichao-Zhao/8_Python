# Gradient Descent Demo
# From Youtube Li Hong-yi DeepLearning lecture
# Lecture title: ML Lecture 1: Regression - Demo
# Date: 2020/02/17

import matplotlib.pyplot as plt
import numpy as np

x_data = [338, 333, 328, 207, 226, 25, 179, 60, 208, 606]
y_data = [640, 633, 619, 393, 428, 27, 193, 66, 226, 1591]

x = np.arange(-200, -100, 1) # bias
y = np.arange(-5, 5, 0.1) # weight
z = np.zeros((len(x), len(y)))
X, Y = np.meshgrid(x, y)
for i in range(len(x)):
    for j in range(len(y)):
        b = x[i]
        w = y[j]
        z[j][i] = 0
        for n in range(len(x_data)):
            z[j][i] = z[j][i] + (y_data[n] - b - w * x_data[n]) ** 2
        z[j][i] = z[j][i]/len(x_data)

# ydata = b + w * xdata
b = -120            # initial b
w = -4              # initial w
lr = 0.00000001     # learning rate
iteration = 100000

# Store initial values for plotting.
b_history = [b]
w_history = [w]

# Iterations
for i in range(iteration):

    b_grad = 0.0
    w_grad = 0.0
    for n in range(len(x_data)):
        b_grad = b_grad - 2.0 * (y_data[n] - b - w * x_data[n]) * 1.0
        w_grad = w_grad - 2.0 * (y_data[n] - b - w * x_data[n]) * x_data[n]
    
    # Update parameters.
    b = b - lr * b_grad
    w = w - lr * w_grad
    
    # Store parameters for plotting.
    b_history.append(b)
    w_history.append(w)

# Plot the figure.
plt.contourf(x,y,z,50,alpha=0.5,cmap = plt.get_cmap('jet'))
# plt.contourf(x,y,z,50,alpha=0.5,cmap=plt.cm.jet)

plt.plot([-188.4], [2.67], 'x', ms=12, markeredgewidth=3, color='orange')
plt.plot(b_history, w_history, 'o-', ms=3, lw=1.5, color = 'black')
plt.xlim(-200, -100)
plt.ylim(-5, 5)
plt.xlabel(r'$b$', fontsize=16)
plt.ylabel(r'$w$', fontsize=16)
plt.show

