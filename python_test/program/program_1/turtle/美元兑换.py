money = input("input money:")
if money[-1] in ['元']:
    dollar = eval(money[0:-1])/7
    print("人民币{}".format(money),"=","美元:{}＄".format(dollar))
elif money[-1] in ['＄']:
    rmb = eval(money[0:-1])*7
    print("美元{}".format(money), "=", "人民币:{}元".format(rmb))