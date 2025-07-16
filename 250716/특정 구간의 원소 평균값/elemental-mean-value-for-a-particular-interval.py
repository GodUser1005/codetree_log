n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
count = 0
for i in range(n):
    for j in range(i,n):
        mean = sum(arr[i:j+1])/(j+1-i)
        for k in range(i,j+1):
            if mean == arr[k]:
                count += 1
                break

print(count)