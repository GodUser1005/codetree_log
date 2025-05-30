a = int(input())
a = a//2 if a % 2 == 0 else a
a = (a+1)//2 if a % 2 == 1 else a
print(a)