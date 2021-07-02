'''COMPUTES THE FIRST N TERMS OF THE 'COUNT AND SAY' SEQUENCE'''

import itertools

n = int(input("Enter the value of n: "))

def fun(x):
    if x == 1:
        return '1'
    else:
        a = []
        l = [''.join(value) for key, value in itertools.groupby(fun(x-1))]
        for i in range(len(l)):
            a.append(len(l[i]))
            a.append(int(l[i][0]))
    return ''.join(str(e) for e in a) # Convert the list into a string
  
for i in range(1, n+1):
    print('For n = {}: {}'.format(i, fun(i)))
