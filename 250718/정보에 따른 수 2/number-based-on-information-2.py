t,a,b = map(int,input().split())
c_list = []
for _ in range(t):
    c,p = input().split()
    p = int(p)
    c_list.append((c,p))

def find_nearleast_s_n(x):
    min_dist_s = 1000
    min_dist_n = 1000
    for c,p in c_list:
        if c == 'S':
            dist = abs(p-x)
            min_dist_s = min(min_dist_s,dist)
        elif c == 'N':
            dist = abs(p-x)
            min_dist_n = min(min_dist_n,dist)
    return min_dist_s,min_dist_n

count = 0
for i in range(a,b+1):
    d1,d2 = find_nearleast_s_n(i)
    if d1 <= d2:
        count += 1

print(count)
    

