import math

def y1(x):
    y=(x**x-3*x)/(x+1)+2*math.pi+math.sin(x)
    return y

def y2(x):
    y= math.log(-5*x,math.e) + 6 * math.sqrt(abs(x) + math.e**4)-(x + 1)**3
    return y

x = int(input("请输入x："))
# 单分支
# if(x>=0):
#     print(y1(x))

# if(x<0):
#     print(y2(x))

# # 双分支
# if(x>=0):
#     print(y1(x))

# else(x<0):
#     print(y2(x))

# 条件运算语句
y = (y1(x)) if(x>=0) else (y2(x))
print(y)
