import random


def randc():
    mi = ''
    u = random.randint(0,62)
    if u>=10:
        if 92<(u+55)<97:
            mi += chr(u+62)
        else:
            mi += chr(u+55)
    else:
        mi += '%d'%u
    return mi

now = ''
for i in range(1,9):
    now += randc()
print(now)