def fun1(h,f):
    r = int(f/2-h)
    c = int(h-r)
    return r,c

def fun2(h,f):
    for c in range(0,h+1):
        r = int(h-c)
        if(2*c+4*r == f):
            break
    return r,c


head = int(input("请输入总头数："))
feet = int(input("请输入总脚数（必须是偶数）："))
while(feet%2 != 0):
    feet = int(input("请输入总脚数（必须是偶数）："))

if head>=0 and feet>=0 and head*2<=feet and head*4>=feet:
    r,c = fun1(head,feet)
    print("方法一：鸡：{0}只，兔：{1}只".format(c,r))
    r,c = fun1(head,feet)
    print("方法二：鸡：{0}只，兔：{1}只".format(c,r))
else:
    print("方法一：无解，请重新运行测试！")
    print("方法二：无解，请重新运行测试！")



