def getValue(b,r,n):
    v = b*((1+r/100)**n)
    return v

money = float(input("请输入本金："))
rate = float(input("请输入年利率："))
year = float(input("请输入年数："))

print(str.format("本金利率和为：{0:2.2f}",getValue(money,rate,year)))