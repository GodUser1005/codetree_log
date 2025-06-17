n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = a[0]
for i in a:
    if min_val > i:
        min_val = i
print(min_val,a.count(min_val))