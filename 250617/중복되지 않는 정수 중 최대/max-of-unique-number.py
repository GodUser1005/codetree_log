n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
count_arr = [0]*1001
for num in nums:
    count_arr[num] += 1

count_1_arr = [i for i in range(1,1001) if count_arr[i] == 1]
if len(count_1_arr) == 0:
    print(-1)
else:
    max_val = count_1_arr[0]
    for num in count_1_arr[1:]:
        if max_val < num:
            max_val = num
    print(max_val)