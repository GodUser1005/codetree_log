n,m = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
for a in arr:
    if a == m:
        cnt += 1

print(cnt)