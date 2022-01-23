#m = 28
#m2 = m
#n = 42
#n2 = n
m = eval(input("m为："))
n = eval(input("n为："))
m2 = m
n2 = n
if m>=n:
    while m%n!=0:
        t = m
        m = n
        n = t%m
    print("最大公约数为：{}\n".format(n))
    print("最小公倍数为：{}".format(m2*n2/n))
else:
    while n%m!=0:
        t = n
        n = m
        m = t%n
    print("最大公约数为：{}\n".format(m))
    print("最小公倍数为：{}".format(m2*n2/m))