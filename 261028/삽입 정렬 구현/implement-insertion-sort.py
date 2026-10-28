def insertion_sort(arr):
    size = len(arr)
    for i in range(1, size):
        j = i - 1
        tmp = arr[i]
        while arr[j] > tmp and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp
    return arr

n = int(input())

arr = list(map(int, input().split()))

ans = insertion_sort(arr)

for e in ans:
    print(e, end=" ")