n = int(input())
for i in range(1,n+1):
    a = i
    for _ in range(n):
        print(a,end="")
        a = n+1 - a
    print()