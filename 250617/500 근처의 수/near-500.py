arr = list(map(int,input().split()))
max_val = 0
min_val = 1001
for a in arr:
    if a > 500 and min_val > a:
        min_val = a
    if a < 500 and max_val < a:
        max_val = a
print(max_val,min_val)