import random

a = random.randint(0,100)
b = random.randint(0,100)
# a = 88
# b = 16

m = a
n = b

if (m < n):
    t = m
    m = n
    n = t

# r = m % n
# while (r != 0):
#     m = n
#     n = r
#     r = m % n
r = 1
while (r != 0):
    r = m % n
    m = n
    n = r

print("a =", a, end=',')
print("b =", b)
print("最大公约数=", m, end=',')
print("最小公倍数=", a*b/m)
