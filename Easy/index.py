import first
import second
import third
import fourth
import fifth
import sixth

import random

while (True):

    print("Input int")
    x = int(input())

    if x == 1:
        q = first.sqr(random.randint(1,100))
        w = first.sqr(random.randint(1,100),1)
        print(q,w)
        break

    elif x == 2:
        print(second.idk(random.randint(0,100)))
        break

    elif x == 3:
        print(third.split("WeLcOmE To ThE JuNgLe"))
        break

    elif x == 4:
        print(fourth.log([1,2,3,4,5,6,7,8,9,10]))
        break

    elif x == 5:
        print(fifth.plus(["Name","SecondName","ThirdName","FifthName"],[1,4,8,8]))
        print(fifth.plus(["Name","SecondName","ThirdName","FifthName"],[1,4,8,8,1488]))
        break

    elif x == 6:
        #Map use func to evert item of list
        array = list(map(int,input().split()))
        print(array)
        print(sixth.sort(array))
        break


    