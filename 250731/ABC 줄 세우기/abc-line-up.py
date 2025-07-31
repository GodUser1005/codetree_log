n = int(input())
arr = list(map(ord,input().split()))
for i in range(n):
    arr[i] = arr[i] - ord('A')

# Please write your code here.
count = 0
for i in range(n):
    for j in range(n):
        if i == arr[j]:
            while i != j:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                j -= 1
                count += 1
            break

print(count)

