import math

def triangle(a):
    for i in range(a):
        a = []
        for j in range(i+1):
            a.append(int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j))))
        print(a)

        