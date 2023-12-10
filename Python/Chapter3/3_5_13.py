sum = 1
# 用for循环
# while(1):
#     n = int(input("请输入非负整数n:"))
#     if(n>=0):
#         for i in range(1,n+1):
#             sum *= i
#         print(sum)
#         break
# 用while循环
while(1):
    n = int(input("请输入非负整数n:"))
    if(n>=0):
        while(n>0):
            sum *= n
            n-=1
        print(sum)
        break


