import sys
MAX_INT = sys.maxsize

n = int(input())
points = [tuple(map(int,input().split())) for _ in range(n)]

min_dist = MAX_INT

def cal_dist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

for j in range(1,n-1):
    dist = 0
    prev_point = points[0]
    for i in range(1,n):
        if i == j:
            continue
        dist += cal_dist(prev_point,points[i])
        prev_point = points[i]
    min_dist = min(dist,min_dist)

print(min_dist)
    

