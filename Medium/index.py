import random

import a
import b
import c
import d
import e
import f
import g
import h
import i
import j
import l
import m
import n
import o
import p
import q
import r
import s
import t



while (True):

    print("\nInput int")
    x = int(input())
    print()

    # max of 3
    if x == 1:
        temp=random.sample(range(0,1000),3)
        print ('Random List:\n',temp)
        print('Max: ',a.mah(temp))

    # sum list (lambda)
    elif x==2:

        temp = random.sample(range(0,1000),random.randint(2,10))
        print ('Random List:\n',temp)
        print('Sum: ',b.Sum(temp))

    # mult list (lambda)
    elif x==3:
        temp = random.sample(range(0,1000),random.randint(2,10))
        print ('Random List:\n',temp)
        print('Mult: ',b.Mult(temp))

    # string reverse
    elif x==4:
        print("Reverse: ",c.Rev(input("Щас будет дичь со срезами (input str):\n")))

    # !(x)
    elif x==5:
        temp = random.randint(1,20)
        print ('Random int(1-20):\n',temp)
        print('Factorial: ',d.fuck(temp))

    # a < X < b
    elif x==6:
        temp1 = random.randint(1,100)
        temp2 = random.randint(1,100)
        temp3 = random.randint(1,100)
        print('Ramdom 3 int:\n',temp1,temp2,temp3)
        print('X: ',e.Whe(temp1,temp2,temp3))

    # Up/Low-case count
    elif x==7:
        print(f.countUpLow(input("Input String:\n")))

    # Unic of list
    elif x==8:
        temp = random.sample([1,2,3,4,5],counts=[10,10,10,10,10],k=5)
        print("Random list:\n",temp)
        print("Unic List",g.Unic(temp))

    # is Simple
    elif x==9:
        temp = random.randint(0,1000)
        print("Random int:\n",temp)

        print(h.simp(temp))

    # even of list
    elif x==10:
        temp = random.sample(range(0,1000),random.randint(2,10))
        print("Random list:\n",temp)

        print("List of even: ",i.foo(temp))

    # is_Perfect()
    elif x==11:
        temp = random.randint(0,1000)
        print("Random int:\n",temp)

        print("Is pErFeCt: ",j.perfect(temp))

    # is_Palindrome
    elif x==12:
        print("Is palindrome: ",l.pal(input("Input String:\n")))
        

    # Pascal Triangle 
    elif x==13:
        temp = random.randint(1,31)
        print("Random int:\n",temp)
        m.triangle(temp)

    # is_pangram    
    elif x==14:
        print("Is pangram: ",n.pang(input("Input pangram:\n")))

    # Split then Sort  
    elif x==15:
        temp = "Lorem/ipsum/dolor/sit/amet/consectetur/adipiscing/elit/Aliquam/non/maximus/est/ac/ullamcorper/lorem/Suspendisse/interdum/condimentum/ligula/et/dictum/odio/viverra/et/Vestibulum/volutpat/nulla/ac/neque/vulputate/tincidunt/Pellentesque/vestibulum/aliquet/tellus/eget/imperdiet/dolor/Quisque/eu/enim/id/neque/imperdiet/faucibus/id/sed/libero/Aliquam/augue"
        print("Input:\n", temp,'\n')
        

        print(o.ss(temp))

    # zip    
    elif x==16:
        print(list(p.x2()))

    #     
    elif x==17:

        temp = input("Input str:\n")
        print(temp,'\n')

        print = q.bold(print)
        print(temp,'\n')

        print = q.Grn(print)
        print(temp,'\n')

        print = q.Underline(print)
        print(temp,'\n')

        print = q.end(print)
        print(temp,'\n')


    # Custome Code
    elif x==18:
        r.wtf(input("Write Code Here:\n"))

    # Func in func??????????
    elif x==19:
        sas = s.test(14)
        print(sas(88))

    # prop at func
    elif x==20:
        print('Prop at func',t.getCount())

        
