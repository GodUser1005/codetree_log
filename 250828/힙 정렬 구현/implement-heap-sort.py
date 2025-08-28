def heapify(arr,i,n):
    if i > n:
        return
    left = 2*i
    right = 2*i + 1
    largest = i

    if n >= right:
        tmp_largest = left
        if arr[left] < arr[right]:
            tmp_largest = right
        if arr[tmp_largest] > arr[largest]:
            tmp_largest,largest = largest, tmp_largest

    elif n >= left:
        tmp_largest = left
        if arr[tmp_largest] > arr[largest]:
            tmp_largest,largest = largest, tmp_largest
    
    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,largest,n)
    


def heap_sort(arr):
    n = len(arr)-1
    for i in range(n//2,0,-1):
        heapify(arr,i,n)
    
    for i in range(n,0,-1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr,1,i-1)


n = int(input())
arr = [0] + list(map(int,input().split()))

heap_sort(arr)
print(" ".join(list(map(str,arr[1:]))))


