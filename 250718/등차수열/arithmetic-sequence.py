n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
def count(k):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] <= k <= a[j] or a[j] <= k <= a[i]:
                if abs(a[i] - k) == abs(a[j] - k):
                    count += 1
    return count

max_count = 0
for i in range(1,101):
    cnt = count(i)
    max_count = max(cnt,max_count)

print(max_count)