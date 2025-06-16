n = int(input())
count_arr = [0 for _ in range(9)]

arr = list(map(int,input().split()))
for a in arr:
    count_arr[a-1] += 1

for count in count_arr:
    print(count)

