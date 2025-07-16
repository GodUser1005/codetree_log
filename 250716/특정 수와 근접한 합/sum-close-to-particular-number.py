import sys
MAX_INT = sys.maxsize

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = MAX_INT
sum = sum(arr)
for i in range(n-1):
    for j in range(i,n):
        temp = sum - arr[i] - arr[j]
        ans = min(abs(s-temp),ans)

print(ans)
