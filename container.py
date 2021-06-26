# FINDS THE MAX AREA CONTAINED BETWEEN BETWEEN VERTICAL LINES

import matplotlib.pyplot as plt
import numpy as np
import random

# Lines heights:
l = [1,8,6,2,5,4,8,3,7]

# Returns the max area and gives the indices of the corresponding lines
def max_area(l):
    u1, u2 = [], []
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            a = min(l[i], l[j])*(j-i)
            u1.append(a)
            u2.append([i, j])
    return max(u1), u2[u1.index(max(u1))]

print('The maximum area is', max_area(l)[0])
print('reached between lines', max_area(l)[1][0], 'and', max_area(l)[1][1])

# Plots. x1, x2 and y give the points to draw the horizontal line
x1 = max_area(l)[1][0]
x2 = max_area(l)[1][1]
y = min(l[x1], l[x2])

x = np.arange(0, len(l))
plt.plot(x, l, 'o')
plt.stem(x, l, markerfmt=' ')  # Plots the vertical lines
plt.plot([x1,x2],[y, y], 'r')  # Plots the horizontal line
plt.show()

'''Finds the expected area and the probability of at least one of the delimiter lines is and endpoint'''
s = []
# Define a counter and the number of trails:
c, n = 0, 1000

for i in range(0, n):
    l = [random.randint(0,10) for i in range(0, 10)] # Gnerates a random sample between 1 and 9 (heights) of size 10
    s.append(max_area(l)[0])
    if max_area(l)[1][0] == 0 or max_area(l)[1][1] == 9:
        c = c + 1
        
print("The expected maximum area is:", sum(s)/n)
print('The probability of a delimiter being one of the endpoints is', c/n)
