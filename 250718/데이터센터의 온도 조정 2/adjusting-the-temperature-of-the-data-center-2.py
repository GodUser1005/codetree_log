n,c,g,h = map(int,input().split())
t_range = [tuple(map(int,input().split())) for _ in range(n)]

MAX_T = 1000

def cal_workload(t1,t2,t):
    if t < t1:
        return c
    elif t <= t2:
        return g
    else:
        return h

max_total_work = 0
for t in range(MAX_T+1):
    total_work = 0
    for i in range(n):
        total_work += cal_workload(t_range[i][0],t_range[i][1],t)
    max_total_work = max(total_work,max_total_work)
print(max_total_work)

