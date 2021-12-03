import math

def log(array):


    for x,y in enumerate(array):
        array[x] = math.log(y)

    return array
