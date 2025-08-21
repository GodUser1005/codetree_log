def insertion_sort(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > val:
                arr[j+1] = arr[j]
                if j == 0:
                    arr[j] = val
            else:
                arr[j+1] = val
                break
    return arr
         

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
sorted_arr = insertion_sort(arr)
print(" ".join(list(map(str,sorted_arr))))
