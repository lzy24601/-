s = [9,7,8,3,2,1,55,6]

for i in range(0,len(s)):
    if s[i]%2==0:
        s[i]= s[i]**2

print(s)