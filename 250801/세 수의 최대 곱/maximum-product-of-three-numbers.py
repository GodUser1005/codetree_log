import sys
MAX_INT = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()

positive_count = 0
for num in arr:
    if num >= 0:
        positive_count += 1

negative_count = n - positive_count

max_product = -MAX_INT
max_product = max((arr[-1]* arr[-2]*arr[-3]),arr[-1]*arr[0]*arr[1])
print(max_product)
    



