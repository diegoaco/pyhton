''' Solves numerically a first-order differential equation of the form
y' = f(x,y)'''

import numpy as np
import matplotlib.pyplot as plt 
import math

# Differential equation
def fun(x,y):
    return x*math.sin(x)
    
def sol(x):    # Analytic solution 
    return math.sin(x) - x*math.cos(x)+ 1

# Parameters of the algorithm:
a, b, n = 0, 30, 1000
h = (b-a)/n

x = np.arange(a, b+h, h)
y = np.zeros(len(x))
y[0] = 1  # Initial condition

# Runge-Kutta method
for i in range(0, len(x)-1):
    k1 = h*fun(x[i], y[i])
    k2 = h*fun(x[i] + h/2, y[i] + h*k1/2)
    k3 = h*fun(x[i] + h/2, y[i] + h*k2/2)
    k4 = h*fun(x[i] + h, y[i] + h*k3)
    y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6

# Plots:
s = np.array([sol(i) for i in x])   # Solution points
plt.plot(x, y, 'or')
plt.plot(x, s)
plt.show()
