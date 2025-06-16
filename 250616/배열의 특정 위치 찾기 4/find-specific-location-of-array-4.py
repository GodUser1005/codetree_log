arr = list(map(int,input().split()))
idx = 10
for i in range(len(arr)):
    if arr[i] == 0:
        idx = i
        break
arr = [a for a in arr[:idx] if a % 2 == 0]
print(len(arr),sum(arr))