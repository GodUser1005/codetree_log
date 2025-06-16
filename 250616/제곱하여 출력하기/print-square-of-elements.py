n = int(input())
arr = list(map(int,input().split()))
arr = [a**2 for a in arr]
for a in arr:
    print(a,end=" ")