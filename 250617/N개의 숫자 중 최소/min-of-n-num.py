n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = a[0]
cnt = 1
for i in a:
    if min_val > i:
        min_val = i
        cnt = 1
    elif min_val == i:
        cnt += 1
print(min_val,cnt)