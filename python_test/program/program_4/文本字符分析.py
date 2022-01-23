txt = input("input:")
counts = {}
ex = {',','.','?'}

for i in txt:
    if i==" " or i in ex:
        continue
    else:
        if ord(i)<97:
            i = chr(ord(i)+32)#将小写字母转化为大写字母
        counts[i] = counts.get(i,0)+1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)#True表示降序，False升序

for u in range(len(items)):
    a,b = items[u]
    print("{}->{}".format(a,b))