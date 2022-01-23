def hanoi(n,a,b,c):
    if n==0:
        return
    hanoi(n-1,a,c,b)
    print("移动{}：将{}借助{}移动到{}。".format(n,a,b,c))
    hanoi(n-1,b,a,c)

n = eval(input("input:"))
hanoi(n,'A','B','C')