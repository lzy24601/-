def mySqrt(a):
    x1 = a/2
    x2 = (x1+a/x1)/2
    while(abs(x1 - x2) >= 1e-6):
        x1 = x2
        x2 = (x1+a/x1)/2

    print("{0}的算数平方根={1:.20f}".format(a,x2))

a = float(input("请输入a:"))
mySqrt(2)