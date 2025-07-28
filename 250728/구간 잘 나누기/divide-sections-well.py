n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
ans = 0
max_sum = sum(a)
for i in range(max_sum,max(a)-1,-1):
    tmp_sum = 0
    count = m - 1
    for j in range(n):
        tmp_sum += a[j]
        if tmp_sum > i:
            count -= 1
            tmp_sum = a[j]
    if count == 0:
        ans = i
print(ans)