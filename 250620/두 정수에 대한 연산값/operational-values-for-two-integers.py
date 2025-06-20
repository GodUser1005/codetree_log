def modify(arr):
    max_idx, min_idx = (0,1) if arr[0] > arr[1] else (1,0)
    arr[max_idx] += 25
    arr[min_idx] *= 2

    


a, b = map(int, input().split())

# Please write your code here.
arr = [a,b]
modify(arr)

for e in arr:
    print(e,end=" ")



