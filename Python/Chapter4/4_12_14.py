import random

# n = random.randint(0,10)
n = 8
s = 0
sn = 0

while(n):
    s = s*10+1
    sn+=s
    n-=1
print(sn)