''' Take n points in R^2 with positive integer entries. Construct n rectangles
with the points and the origin being opposite vertices. Find the one with
the largest area such that it does not contain another point in its interior.'''

import numpy as np
import random as rd
import matplotlib.pyplot as plt

# Generates two lists of size n for the x and y coordinates (otherwise, they must be given):
n, x, y = 15, [], []
for i in range(0, n):
    x.append(rd.randint(1,30))
    y.append(rd.randint(1,30))

# (Optional) Plots the rectangles:
plt.scatter(x,y)
plt.vlines(x, 0, y, color='red')
plt.hlines(y, 0, x, color='red') 
plt.show()

# Takes the two lists and finds the points not having another points in their interior by using a counter: 
def rect(x,y):
    xnew, ynew = [], []
    for i in range(0, len(x)):
        c = 0
        for j in range(0, len(y)):
            if x[i] <= x[j] or y[i] <=y[j]: c = c+1
            if c == n:  # Only the points with c = n survive
                xnew.append(x[i]), ynew.append(y[i])
    return xnew, ynew

def area(l):
    xnew, ynew = l[0], l[1]
    areas = list(np.multiply(xnew, ynew))
    max_index = areas.index(max(areas))
    return areas, max(areas), max_index

print('Point:', [rect(x,y)[0][area(rect(x,y))[2]], rect(x,y)[1][area(rect(x,y))[2]]],
      '\n' 'Area:', area(rect(x,y))[1])
