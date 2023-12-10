#要打印的行数
# n = int(input("请输入要打印的行数："))

# i_list = [1]
# str_list = []

# for i in range(1,n+1):
#     if i == 1:
#         str_list.append(' '.join(str(a) for a in i_list))
#     else:
#         ii_list = [1]
#         for j in range(1,i-1):
#             ii_list.append(i_list[j-1]+i_list[j])
#         ii_list.append(1)
#         i_list = ii_list
#         str_list.append(' '.join(str(a) for a in i_list))

def factorial(n):

    return 1 if n==0 else n*factorial(n-1)
    # if n == 0:
    #     return 1
    # else:
    #     return n*factorial(n-1)
    
print(factorial(3))
