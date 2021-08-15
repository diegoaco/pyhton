''' There are n passengers queueing to board a plane, each with an assigned seat. However, the first
passenger chooses a random seat. The rest of the passengers will be seated as follows: if avaialble, they
will take their seats; otherwise, they will select one at random. What is the probability the last person
finds their seat free? '''

import random as rd
    
c, k = 0, 0
t = 10000 # number of trials
n = 10 # number of passengers

c = 0
for i in range(1,t+1):
    l = [rd.randint(1, n)]  # Assign a random seat to the 1st passenger
    for i in range(1, n):
        # Now for the rest of the passengers:
        # If their seat is occupied, assign a random one that has not been taken yet:
        if i+1 in l:
            l.append(rd.choice([x for x in range(1,n+1) if x not in l]))
        # Otherwise, give them their seat:
        else:
            l.append(i+1)
    # Finally, check if the last passenger has their seat:
    if l[-1] == n:
        c = c+1
        
print('Probability the last person gets their seat:', c/t)
