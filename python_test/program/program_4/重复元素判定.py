def getc(lista):
    counts = {}
    for cou in lista:
        counts[cou] = counts.get(cou,0)+1
    return counts

str1 = input("input")
str2 = getc(str1)
for i in str2:
    if str2[i]>1:
        print("True")
    else:
        print("False")
