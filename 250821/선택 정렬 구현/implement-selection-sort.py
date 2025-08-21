
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        # 가장 작은 값의 인덱스 찾기
        for j in range(i+1,n):
            if arr[min_i] > arr[j]:
                min_i = j
        
        # 맨 앞과 가장 작은값을 바꿔주기
        if arr[i] != arr[min_i]:
            arr[i],arr[min_i] = arr[min_i],arr[i]
    
    return arr
            


n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
answer = map(str,selection_sort(arr))
print(" ".join(answer))


