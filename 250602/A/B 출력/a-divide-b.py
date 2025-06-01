a,b = map(int,input().split())
print(a//b,end=".")
a = (a % b)*10
for _ in range(20):
    print(a//b,end="")
    a = (a % b)*10