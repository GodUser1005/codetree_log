def absolute(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = -1*arr[i]

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

absolute(arr)

for e in arr:
    print(e,end=" ")