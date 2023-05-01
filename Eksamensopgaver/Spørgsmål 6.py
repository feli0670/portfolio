import math
def f1 (a,b,c):
    x = math.sqrt((a+1)/(b-1)-c)
    print(x)


def f2(a,b,c):
    try:
        f1(a,b,c)

    except ZeroDivisionError:
        print('hej')

f2(1,1,1)