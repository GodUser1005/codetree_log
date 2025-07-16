import sys
MAX_INT = sys.maxsize

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = MAX_INT
for i in range(n-1):
    for j in range(i+1,n):
        temp = sum(arr) - arr[i] - arr[j]
        ans = min(abs(s-temp),ans)

print(ans)
