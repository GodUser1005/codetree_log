import sys
MAX_INT = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
min_sum = MAX_INT
for i in range(n):
    for j in range(n):
        tmp = arr[:]
        tmp[i] *= 2
        summ = 0
        for k in range(n-1):
            if k == j:
                continue
            elif k == j-1 and j+1 < n:
                summ += abs(tmp[k] - tmp[k+2])
            else:
                summ += abs(tmp[k] - tmp[k+1])
        min_sum = min(min_sum,summ)
            
print(min_sum)