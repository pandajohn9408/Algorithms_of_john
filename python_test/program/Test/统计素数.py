a = []
for n in range(100,201):
    k = False
    for i in range(2,n):
        if n%i==0:
            break
        else:
            k = True
    if k:
        a.append(n)
print(a)


