def countUpLow(a):
    u = sum(1 for i in a if i.isupper())
    l = sum(1 for i in a if i.islower())

    return("UpperCase: %s \nLowerCase: %s" %(u,l))