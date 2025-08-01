n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
front = arr[:n]
back = arr[n:]

print(min([back[i] - front[i] for i in range(n)]))