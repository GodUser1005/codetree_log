import sys
MAX_INT = sys.maxsize

n,h,t = map(int,input().split())
field = list(map(int,input().split()))

min_cost = MAX_INT
for i in range(n-t+1):
    cost = 0
    for k in range(i,i+t):
        cost += abs(field[k]-h)
    min_cost = min(cost,min_cost)

print(min_cost)


