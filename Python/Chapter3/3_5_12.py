import math

def func(a,b,c):
    if(a==0 and b==0):
        print("此方程无解!")
    elif(a==0 and b!=0):
        print(str.format("此方程的解为：{}",-c/b))
    elif(b**2-4*a*c==0):
        print("此方程有两个相等实根：",-b/2/a)
    elif(b**2-4*a*c>0):
        print(str.format("此方程有两个不等实根：{0} 和 {1}",-b/2/a+math.sqrt(b**2-4*a*c)/2/a,-b/2/a-math.sqrt(b**2-4*a*c)/2/a))
    else:
        print(str.format("此方程有两个不等虚根：{0}+{1}i 和 {0}-{1}i",-b/2/a,math.sqrt(4*a*c-b**2)/2/a))

a = float(input("请输入系数a："))
b = float(input("请输入系数b："))
c = float(input("请输入系数c："))

func(a,b,c)
