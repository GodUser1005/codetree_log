def merge(arr, low, mid, high):
    left_i = low
    right_i = mid+1

    new_arr = []
    while left_i <= mid and right_i <= high:
        if arr[left_i] < arr[right_i]:
            new_arr.append(arr[left_i])
            left_i += 1
        else:
            new_arr.append(arr[right_i])
            right_i += 1

    if left_i > mid:
        for i in range(right_i,high+1):
            new_arr.append(arr[i])
    else:
        for i in range(left_i,mid+1):
            new_arr.append(arr[i])
    
    for i in range(len(new_arr)):
        arr[low+i] = new_arr[i]




def merge_sort(arr, low, mid, high):
    if low < high:
        merge_sort(arr, low, (low+mid) // 2, mid)
        merge_sort(arr, mid+1, (mid+1 + high) // 2, high)
        merge(arr, low, mid, high)



n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
merge_sort(arr,0, (len(arr)-1) // 2 ,len(arr)-1)
print(" ".join(list(map(str,arr))))
