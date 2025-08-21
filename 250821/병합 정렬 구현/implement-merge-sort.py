def merge(left,right):
    left_i, right_i = 0,0
    new_arr = []
    while not (left_i == len(left) or right_i == len(right)):
        left_num = left[left_i]
        right_num = right[right_i]
        if left_num < right_num:
            new_arr.append(left_num)
            left_i += 1
        else:
            new_arr.append(right_num)
            right_i += 1
    
    if left_i == len(left):
        new_arr += right[right_i:]
    else:
        new_arr += left[left_i:]
    return new_arr



def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    left = merge_sort(arr[:n//2])
    right = merge_sort(arr[n//2:])
    arr = merge(left,right)
    return arr


n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
sorted_arr = merge_sort(arr)
print(" ".join(list(map(str,sorted_arr))))
