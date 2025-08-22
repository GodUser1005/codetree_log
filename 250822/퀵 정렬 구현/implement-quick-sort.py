def quick_sort(arr, low, high):
    if low < high:
        pivot_i = high
        pivot_num = arr[high]

        cur = low-1 
        for i in range(low,high):
            if pivot_num > arr[i]:
                cur += 1
                if cur != i:
                    arr[i], arr[cur] = arr[cur], arr[i]
        
        cur += 1
        arr[cur], arr[pivot_i] = arr[pivot_i], arr[cur]
        quick_sort(arr,low,cur-1)
        quick_sort(arr,cur+1,high)
    

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
quick_sort(arr,0,len(arr)-1)
print(" ".join(list(map(str,arr))))

