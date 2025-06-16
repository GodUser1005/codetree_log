count_arr = [0]*7
arr = list(map(int,input().split()))
for a in arr:
    count_arr[a] += 1

for i in range(1,len(count_arr)):
    print(f"{i} - {count_arr[i]}")