import random

def sort_1(a,b,c):
    sum = a+b+c
    a = min(a,b,c)
    c = max(a,b,c)
    b = sum - a -c 
    print("(方法一)升序值：a={0},b={1},c={2}".format(a,b,c))

def sort_2(a,b,c):
    abc=[a,b,c]
    abc = sorted(abc)
    print("(方法二)升序值：a={0},b={1},c={2}".format(abc[0],abc[1],abc[2]))

a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)

print("原始值：a={0},b={1},c={2}".format(a,b,c))
sort_1(a,b,c)
sort_2(a,b,c)