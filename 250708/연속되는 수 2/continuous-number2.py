n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
num = arr[0]
count = 1
max_count = 0

for i in range(1,n):
    if num == arr[i]:
        count += 1
        if max_count < count:
            max_count = count
    else:
        num = arr[i]
        count = 1

print(max_count)
    