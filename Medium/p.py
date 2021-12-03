def x2():
    count = []
    countX2 = []
    
    for i in range(1,31):
        count.append(i)
        countX2.append(i*i)
    
    return zip(count,countX2)