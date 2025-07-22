n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
min_count = n

for x in range(0,101,2):
    for y in range(0,101,2):
        region_count = [0] * 5
        for point in points:
            x_,y_ = point
            if x_ > x:
                if y_ > y:
                    region_count[1] += 1
                else:
                    region_count[4] += 1
            else:
                if y_ > y:
                    region_count[2] += 1
                else:
                    region_count[3] += 1
        min_count = min(min_count,max(region_count))
print(min_count)
