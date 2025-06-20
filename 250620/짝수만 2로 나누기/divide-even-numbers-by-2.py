def modify(array):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i] //= 2

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

modify(arr)
for e in arr:
    print(e,end=" ")