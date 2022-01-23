def multi(a,*b):
    num = a
    for i in b:
        num *= i
    return num

num = multi(1,2,3,4)

print(num)