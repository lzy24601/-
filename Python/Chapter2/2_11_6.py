import datetime

sName = input("请输入您的姓名：")
birtYear = int(input("请输入您的出生年份："))

age = datetime.date.today().year-birtYear

print("您好！{0}。您{1}岁。".format(sName,age))