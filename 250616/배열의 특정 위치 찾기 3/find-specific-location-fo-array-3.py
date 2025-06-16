arr = list(map(int,input().split()))
idx = 0
for i in range(len(arr)):
    if arr[i] == 0:
        idx = i
        break
arr = arr[idx-3:idx]
print(sum(arr))