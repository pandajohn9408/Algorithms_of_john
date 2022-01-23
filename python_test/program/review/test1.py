import math


def isPrime(s):
    try:
        if type(s)==type(0.):
            raise TypeError
        r = math.floor(math.sqrt(s))
    except TypeError:
        print("输入的不是一个整数")
    if s==0:
        return False
    else:
        for i in range(2,r+1):
            if s%i==0:
                return False
        return True

print(isPrime(10))