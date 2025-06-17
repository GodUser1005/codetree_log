n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_idx = n
while max_idx > 0:
    max_val = a[0]
    max_idx = 0
    for i in range(1,len(a)):
        if a[i] > max_val:
            max_val = a[i]
            max_idx = i
    print(max_idx + 1,end=" ")
    a = a[:max_idx]
