def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def pow_e(x):
    sum = 0
    n = 0
    flag = 1
    item_n = 1
    while(flag and abs(item_n)>=1e-6):
        sum+=item_n
        n+=1
        item_n = x**n/factorial(n)
    return sum
x = int(input("请输入x："))
print("Pow(e,x) = ",pow_e(x))


