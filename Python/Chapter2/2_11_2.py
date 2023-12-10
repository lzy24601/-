money = float(input("请输入本金："))
rate = float(input("请输入年利率："))
year = float(input("请输入年数："))
amount = money*(1+rate/100)**year
print(str.format("本金利率和为：{0:2.2f}",amount))