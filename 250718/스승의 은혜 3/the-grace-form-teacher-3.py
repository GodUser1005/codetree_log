n,b = map(int,input().split())
p = []
s = []
for i in range(n):
    pi,si = map(int,input().split())
    p.append(pi)
    s.append(si)

max_count = 0
for i in range(n):
    temp = p[:]
    temp[i] //= 2
    total_cost = [temp[j] + s[j] for j in range(n)]
    total_cost.sort()
    tmp_b = b
    c = 0
    for j in range(1,n+1):
        tmp_b -= total_cost[j-1]
        if tmp_b >= 0:
            c = j
    max_count = max(c,max_count)

print(max_count)
