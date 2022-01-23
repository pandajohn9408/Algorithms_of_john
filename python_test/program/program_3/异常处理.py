import math
def isPrime(num):
    try:
        if type(num)==type(0.):
            raise TypeError
        r = math.floor(math.sqrt(num))#求其平方根,向下取整
    except TypeError:
        print("输入的不是整数")
    if num==0:
        return False
    else:
        for i in range(2,r+1):
            if num%i==0:
                return False
        return True

n = eval(input("input:"))
print(isPrime(n))