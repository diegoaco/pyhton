'''An old exercise to understand functions in Python'''

a,b = [float(x) for x in input('Enter a and b separated by a comma:').split(',')]

def calc(a,b):
    assert b != 0, 'Division cannot be performed'
    x = a+b
    y = a-b
    z = a*b
    w = a/b
    return (x,y,z,w)

print(calc(a,b))
