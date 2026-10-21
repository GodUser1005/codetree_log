def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_i = i
        for j in range(i + 1, size):
            if arr[min_i] > arr[j]:
                min_i = j
        if min_i != i:
            arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr
            



n = int(input())
arr = list(map(int, input().split()))

arr = selection_sort(arr)

for num in arr:
    print(num, end=" ")



