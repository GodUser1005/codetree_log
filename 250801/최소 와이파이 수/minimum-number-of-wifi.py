n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
count = 0
tmp = arr[:]

i = 0
while i < n:
    if tmp[i] == 1:
        i += 2*m
        count += 1
    i += 1

print(count)
