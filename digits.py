# Practice exercise. Takes the numbers from 0 to n, multiplies the digits of each number 
# (0 becomes 1 ) and then adds them up.

import math

def fun(n):
    t = 0     # Starting point of the sum
    for i in range(0,n):
        i = str(i)      # The key is to transform the number into a string
        i = i.replace('0','1')      # Zeros are replaced by ones
        s = math.prod(int(x) for x in i if x.isdigit())     # Multiplies the digits
        t = t+s     # Cumulative sum
    return t

print(fun(100))
