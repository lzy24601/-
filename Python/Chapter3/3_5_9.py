# 矩形块
for i in range(1, 10):
    s = ""
    for j in range(1,10):
        s += str.format("{0:1}*{1:1}={2:<3}",i,j,i * j)
    
    print(s)

# 下三角
# for i in range(1, 10):
#     s = ""
#     for j in range(1,i+1):
#         s += str.format("{0:1}*{1:1}={2:<3}",i,j,i * j)
    
#     print(s)


#上三角
# for i in range(1,10):
#     s=""
#     for j in range(0,i-1):
#         s+= ' '*7
#     for k in range(i,10):
#         s+=str.format("{0:1}*{1:1}={2:<3}",i,k,i * k)

#     print(s)