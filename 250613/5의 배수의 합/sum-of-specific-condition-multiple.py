a,b = map(int,input().split())
if a > b:
    a,b = b,a
s = 0
for i in range(a,b+1):
    if i % 5 == 0:
        s += i
print(s)