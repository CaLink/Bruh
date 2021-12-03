from functools import reduce

def Sum(a):
    return reduce(lambda x,y: x+y, a)

def Mult(a):
    return reduce(lambda x,y: x*y, a)
