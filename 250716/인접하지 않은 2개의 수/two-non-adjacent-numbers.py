import sys
MIN_INT = -sys.maxsize

n = int(input())
numbers = list(map(int,input().split()))

max_sum = MIN_INT
for i in range(n-2):
    first_num = numbers[i]
    for j in range(i+2,n):
        max_sum = max(max_sum,first_num + numbers[j])

print(max_sum)
