import sys
MIN_INT = -sys.maxsize

n,k = map(int,input().split())
arr = [0] * 10001

ans = MIN_INT
for _ in range(n):
    p,c = input().split()
    p = int(p)
    arr[p] = c


for i in range(1,10000-k+1):
    point = 0
    for j in range(k+1):
        if arr[i+j] == 'G':
            point += 1
        elif arr[i+j] == 'H':
            point += 2
    ans = max(point,ans)

print(ans)
