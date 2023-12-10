import math

A = int(input("请输入直角三角形的直角边A(>0):"))
B = int(input("请输入直角三角形的直角边B(>0):"))
C = math.sqrt(A**2+B**2)

print("直角三角形的三边分别为a={0:1.1f}，b={1:1.1f}，c={2:1.1f}".format(A,B,C))

p = A+B+C
area = A*B/2
print("三角形的周长 = {0:1.1f}，面积 = {1:1.1f}".format(p,area))
sinA = round(math.asin(A/C)*180/math.pi,0)
sinB = round(math.asin(B/C)*180/math.pi,0)

print("三角形两个锐角的度数分别为：{0}和{1}".format(sinA,sinB))




