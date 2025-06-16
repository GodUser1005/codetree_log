arr = list(map(int,input().split()))
idx = 10
for i in range(len(arr)):
    if arr[i] == 0:
        idx = i
for i in arr[idx-1::-1]:
    print(i,end=" ")
