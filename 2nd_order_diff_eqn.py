''' Solves numerically a 2nd order differential equation of the form
y' = f(x, y, y'). It defines y = y1 and y' = y2, leading to the 1st
order system
y1' = y2,
y2' = f(x, y1, y2) '''

import numpy as np
import matplotlib.pyplot as plt 
import math

# Equations set-up
def fun1(x, y1, y2):
    return y2

def fun2(x, y1, y2):
    return y1*y2 - 3*y1 + math.sin(x)

# Partition:
a, b, n = 0, 20, 10000
h = (b-a)/n

x = np.arange(a, b + h, h)
y1 = np.zeros(len(x))
y2 = np.zeros(len(x))
y1[0], y2[0] = 0, 1    # Intial conditions

# Runge-Kutta method
for i in range(0, len(x)-1):
    k11 = h*fun1(x[i], y1[i], y2[i])
    k21 = h*fun2(x[i], y1[i], y2[i])
    
    k12 = h*fun1(x[i] + h/2, y1[i] + h*k11/2, y2[i] + h*k21/2)
    k22 = h*fun2(x[i] + h/2, y1[i] + h*k11/2, y2[i] + h*k21/2)

    k13 = h*fun1(x[i] + h/2, y1[i] + h*k12/2, y2[i] + h*k22/2)
    k23 = h*fun2(x[i] + h/2, y1[i] + h*k12/2, y2[i] + h*k22/2)
    
    k14 = h*fun1(x[i] + h, y1[i] + h*k13, y2[i] + h*k23)
    k24 = h*fun2(x[i] + h, y1[i] + h*k13, y2[i] + h*k23)
    
    y1[i+1] = y1[i] + (k11 + 2*k12 + 2*k13 + k14)/6
    y2[i+1] = y2[i] + (k21 + 2*k22 + 2*k23 + k24)/6

# Plots of y and y':
plt.plot(x, y1, 'blue')
plt.plot(x, y2, 'red')
plt.show()
# Plots the phase space diagram:
#plt.plot(y1, y2)
#plt.show()
