arr = list(map(int,input().split()))
max_val = arr[0]
for a in arr[1:]:
    if max_val < a:
        max_val = a
print(max_val)