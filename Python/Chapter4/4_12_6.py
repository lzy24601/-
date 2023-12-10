x = float(input("请输入操作数x:"))
y = float(input("请输入操作数y:"))
operationSymbol = input("请输入操作符")

def add(x,y):
    print("{0}+{1}={2}".format(x,y,x+y))

def minus(x,y):
    print("{0}-{1}={2}".format(x,y,x-y))

def multiply(x,y):
    print("{0}*{1}={2}".format(x,y,x*y))

def divide(x,y):
    if y == 0:
        print("分母=0，零除异常!")
    else:
        print("{0}/{1}={2}".format(x,y,x/y))
    
def mod(x,y):
    if y == 0:
        print("分母=0，零除异常!")
    else:
        print("{0}%{1}={2}".format(x,y,x%y))

if operationSymbol == '+':
    add(x,y)
elif operationSymbol == '-':
    minus(x,y)
elif operationSymbol == '*':
    multiply(x,y)
elif operationSymbol == '/':
    divide(x,y)
elif operationSymbol == '%':
    mod(x,y)
