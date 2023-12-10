def Sn(n):
    flag = 1
    sum = 0
    for i in range(1,n+1):
        if(i % 2 ==1):
            sum += i*flag
            flag *= -1
    
    return sum 
n = int(input())
print(Sn(n))