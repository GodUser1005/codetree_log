def modify(a,b):
    arr = [a,b]
    min_idx,max_idx = (0,1) if a < b else (1,0)
    arr[min_idx] += 10
    arr[max_idx] *= 2
    return arr

a, b = map(int, input().split())

# Please write your code here.

a,b = modify(a,b)
print(a,b)