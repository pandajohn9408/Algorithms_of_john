from random import random, randint

right = randint(0,9)
num = 10
count = 0
while num!=right:
    num = eval(input("input your guess："))
    if num>right:
        print("It's too big\n")
        count+=1
    elif num<right:
        print("It's too small\n")
        count+=1
count+=1
print("It's right!,and you guess {}".format(count))