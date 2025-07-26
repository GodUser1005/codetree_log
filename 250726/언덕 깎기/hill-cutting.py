import sys
MAX_INT = sys.maxsize

n = int(input())
hills = [int(input()) for _ in range(n)]

min_cost = MAX_INT 
for m in range(0,101-17):
    cost = 0
    for h in hills:
        if h < m:
            cost += abs(h-m)**2
        elif h > m+17:
            cost += abs(h - (m+17))**2
    min_cost = min(cost,min_cost)

print(min_cost)
            

