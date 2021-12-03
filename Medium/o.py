from functools import reduce

def ss(a):
    a=sorted(a.split('/'))

   

    return reduce(lambda x,y: x+'-'+y,a)