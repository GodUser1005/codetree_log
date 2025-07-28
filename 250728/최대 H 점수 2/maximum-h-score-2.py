n,l = map(int,input().split())
arr = list(map(int,input().split()))

def cal_h():
    for i in range(1,n+1):
        cnt = 0
        for j in range(n):
            if arr[j] >= i:
                cnt += 1
        if cnt < i:
            return i,cnt
    return n,0

ans = 0
a,b = cal_h()

if a == n and b == 0:
    ans = n
elif a-b > l:
    ans = a-1
else:
    ans = a

print(ans)

