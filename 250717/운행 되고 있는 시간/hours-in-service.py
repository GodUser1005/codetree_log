MAX_TIME = 1000
n = int(input())
start = []
end = []
for _ in range(n):
    s,e = map(int,input().split())
    start.append(s)
    end.append(e)

max_t = 0
for i in range(n):
    time_line = [0] * (MAX_TIME + 1)
    for j in range(n):
        if i == j:
            continue
        s,e = start[j],end[j]
        for k in range(s,e):
            time_line[k] = 1
    total_time = sum(time_line)
    max_t = max(max_t,total_time)
print(max_t)
