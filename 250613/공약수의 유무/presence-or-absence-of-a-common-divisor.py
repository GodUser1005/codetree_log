a,b = map(int,input().split())
isExist = False
for i in range(a,b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        isExist = True
        break
print(int(isExist))