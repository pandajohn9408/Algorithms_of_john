a = input("input:")
en=num=space=other=ch= 0
for i in a:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        en+=1
    elif '0'<=i<='9':
        num+=1
    elif i==' ':
        space+=1
    elif i.isalpha():
        ch+=1
    else:
        other+=1
print("共有英文字符：{}个\n".format(en),"中文字符：{}".format(ch),"数字：{}个\n".format(num),"空格：{}\n".format(space),"其他：{}\n".format(other))