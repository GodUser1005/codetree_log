n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

count = 0
count_arr = []

for i in range(n):
    if t < arr[i]:
        count += 1
    else:
        count_arr.append(count)
        count = 0
count_arr.append(count)

print(max(count_arr))