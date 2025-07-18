n = int(input())
h = [int(input()) for _ in range(n)]

def count_iceberg(height):
    count = 0
    ice_h = [i-height if i > height else 0 for i in h]
    for i in range(len(ice_h)-1):
        if ice_h[i] == 0 and ice_h[i+1] > 0:
            count += 1
    if ice_h[0] > 0:
        count += 1
    return count

max_ice = 0
for i in range(1,1001):
    max_ice = max(max_ice,count_iceberg(i))

print(max_ice)