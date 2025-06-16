a,b = map(int,input().split())
print(a,b,end=" ")
for i in range(8):
    temp = a+b
    temp %= 10
    print(temp,end=" ")
    a = b
    b = temp