arr = list(map(int,input().split()))
idx = 0
for i in range(len(arr)):
    if arr[i] == 0:
        idx = i
        break
arr = [a+3 if a % 2 == 1 else a//2 for a in arr[:idx]]
for i in arr:
    print(i,end=" ")