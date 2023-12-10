def fun1(s):
    s = list(set(s))
    print(s)

def fun2(s):
    ss = []
    for i in s:
        if i not in ss:
            ss.append(i)
    
    print(ss)


s = [1,2,3,4,5,6,1,2,12,4,5,6,7,6,7,5,4]
fun1(s)
fun2(s)