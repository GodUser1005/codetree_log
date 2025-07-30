n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

tmp = 0
ans = 0
for i in range(n):
    ans += tmp
    if a[i] > b[i]:
        tmp += a[i] - b[i]
        a[i] = b[i]
    else:
        tmp -= b[i] - a[i]
        a[i] = b[i]

print(ans)