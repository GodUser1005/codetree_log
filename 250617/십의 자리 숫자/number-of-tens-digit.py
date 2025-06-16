arr = list(map(int,input().split()))
count_arr = [0]*10
idx = 0
for a in arr:
    if a == 0:
        break
    count_arr[a//10] += 1
for i in range(1,len(count_arr)):
    print(f"{i} - {count_arr[i]}")