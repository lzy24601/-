import math

def area(a,b,c):
    h = (a+b+c)/2
    return math.sqrt(h*(h-a)*(h-b)*(h-c))

def circumance(a,b,c) :
    return a+b+C

A = float(input("请输入三角的边长A:"))
B = float(input("请输入三角的边长B:"))
C = float(input("请输入三角的边长C:"))

if(A>0 and B>0 and C>0 and A+B>C and A+C>B and B+C>A):
    print(str.format("三角形的三边分别为：a={0}, b={1}, c={2}",A,B,C))
    print(str.format("三角形的周长={0}，面积={1}",circumance(A,B,C),area(A,B,C)))
