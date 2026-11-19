import math
PI = math.pi
def circle(r):
    zc = 2*PI*r
    mj = PI*r*r
    print("圆的周长为：" + str(zc) + ",面积为：" + str(mj))

def square(a, b, c):
    zc = (a + b + c)*2
    mj = a*b*c
    print("矩形的周长为：" + str(zc) + ",面积为：" + str(mj))

