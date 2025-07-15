import sys
MAX_INT = sys.maxsize

n = int(input())
n_people = [int(input()) for _ in range(n)]

min_dist = MAX_INT

for start in range(n):   
    dist = 0
    for i in range(n):
        dist += n_people[(start+i) % n] * i
    min_dist = min(dist,min_dist)

print(min_dist)

