n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def is_equal_list(arr1,arr2):
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

b.sort()
count = 0
for i in range(n-m+1):
    arr = a[i:i+m]
    arr.sort()
    if is_equal_list(arr,b):
        count += 1

print(count)
