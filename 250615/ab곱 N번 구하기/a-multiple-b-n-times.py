n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    prod = 1
    for j in range(a,b+1):
        prod *= j
    print(prod)