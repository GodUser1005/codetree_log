n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
min_cost = 100 * 10000
for m in range(min(arr),max(arr)-k+1):
    cost = 0
    for i in arr:
        if i < m:
            cost += m-i
        elif m + k < i:
            cost += i - (m+k)
    min_cost = min(cost,min_cost)

print(min_cost)
    