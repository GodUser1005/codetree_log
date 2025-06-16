n = int(input())
arr = list(map(int,input().split()))
arr = [a for a in arr[::-1] if a % 2 == 0]
for a in arr:
    print(a,end=" ")