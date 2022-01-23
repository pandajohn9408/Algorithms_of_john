from random import randint, choice

a = 0#门1，1表示后面有车，0表示山羊
b = 0#门2
c = 0#门3
zcr

def createYCM():
    global a,b,c#申明全局变量
    while a==0 or b==0 or c==0:
        a = randint(0,1)
        b = randint(0, 1)
        c = randint(0, 1)
        if a==1 and b ==0 and c==0:
            break
        elif a==0 and b==1 and c==0:
            break
        elif a==0 and b==0 and c==1:
            break

def choose():
    lista = ['a','b','c']
    guess1 = choice(lista)
    while 1:
        if guess1 == 'a':
            global a
            if a==1:
                continue
            else:
                print("a")

                break
        elif guess1 == 'b':
            global b
            if b==1:
                continue
            else:
                print("b")
        elif guess1 == 'c':
            global c
            if b==1:
                continue
            else:
                print("c")
                return 'c'





createYCM()
guess = input("选门：")
print("主持人开启一扇门(没有山羊)")
print("主持人选择的是：",zcr)