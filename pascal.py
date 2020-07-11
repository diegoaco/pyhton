# Produces, recursively, the first n rows of the Pascal triangle

def pascal(n):
    x = [1]     # Define the first element of the row
    # Base case
    if  n == 0:
        return [1]
    else:
        l = pascal(n-1)
        print(l)    # Print the rows
        for i in range(0, len(l)-1):
            x.append(l[i] + l[i+1])
        x.append(1)     # Attach the last 1
        return x

print(pascal(10))
