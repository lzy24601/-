def ballFall(h,n):
    sum = 0
    for i in range(1,n+1):
        bound_h = h
        sum += h
        h = h/2
    print("小球在第{}次落地时，共经过{:.2f}米".format(n,sum))
    print("第{}次反弹{:.2f}米".format(n,bound_h))

ballFall(100,10)