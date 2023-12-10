def isTriangle(a,b,c):
    if a+b>c:
        return 1
    else:
        return 0

def isIsocelesTriangle(a,b,c):
    if a==b and a != c:
        print("该三角形为等腰三角形！")

def isEquilateralTtiangle(a,b,c):
    if a == b and a == c:
        print("该三角形为等边三角形！")

def isRightangledTriangle(a,b,c):
    if c**2 == a**2+b**2:
        print("该三角形为直角三角形！")


a = int(input("请输入三角形的边a："))
b = int(input("请输入三角形的边b："))
c = int(input("请输入三角形的边c："))

sum = a+b+c
a = min(a,b,c)
c = max(a,b,c)
b = sum-a-c

if isTriangle(a,b,c):
    isIsocelesTriangle(a,b,c)
    isEquilateralTtiangle(a,b,c)
    isRightangledTriangle(a,b,c)
else:
    print("无法构成三角形！")