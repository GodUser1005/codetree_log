import sys
MAX_INT = sys.maxsize

n = int(input())
x_list = []
y_list = []

for _ in range(n):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

min_dist = MAX_INT
for i in range(n):
    for j in range(i+1,n):
        dx = x_list[i]-x_list[j]
        dy = y_list[i]-y_list[j]
        dist = dx**2 + dy**2
        min_dist = min(dist,min_dist)
print(min_dist)
