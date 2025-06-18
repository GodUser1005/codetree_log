arr = [len(input()) for _ in range(3)]

max_len = arr[0]
min_len = arr[0]

for a in arr:
    if max_len < a:
        max_len = a
    if min_len > a:
        min_len = a

print(max_len-min_len)