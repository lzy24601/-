salary = int(input("请输入有固定工资收入的党员的月工资："))
if salary <= 3000:
    feerate = 0.005
elif salary>3000 and salary<=5000:
    feerate = 0.01
elif salary>5000 and salary<=10000:
    feerate = 0.15
elif salary >10000:
    feerate = 0.02

fee = salary*feerate
print("月工资 = {0},交纳党费 = {1}".format(salary,fee))