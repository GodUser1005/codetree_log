import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int,input().split()))

min_distance = INT_MAX
for i in range(n):
    distance = 0
    for j in range(n):
        distance += (abs(i-j) * arr[j])
    if min_distance > distance:
        min_distance = distance

print(min_distance)