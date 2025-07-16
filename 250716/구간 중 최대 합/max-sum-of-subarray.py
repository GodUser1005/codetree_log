import sys
MIN_INT = -sys.maxsize

n,k = map(int,input().split())
numbers = list(map(int,input().split()))

ans = MIN_INT
for i in range(n-k):
    ans = max(ans,sum(numbers[i:i+k]))

print(ans)


