n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def insertion_sort(arr):
    sorted_arr = [arr[0]]
    print(sorted_arr[0],end=" ")
    for i in range(1,n):
        index = len(sorted_arr)
        for j in range(len(sorted_arr)-1,-1,-1):
            if arr[i] >= sorted_arr[j]:
                break
            index -= 1
        sorted_arr.insert(index,arr[i])
        if len(sorted_arr) % 2 == 1:
            print(sorted_arr[len(sorted_arr) // 2],end=" ")

insertion_sort(arr)