n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

num = arr[0]
count = 1
count_arr = []

for i in range(1,n):
    if num < arr[i]:
        count += 1
    else:
        count_arr.append(count)
        count = 1
    num = arr[i]
count_arr.append(count)

print(max(count_arr))