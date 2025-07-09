N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

a = [0]
b = [0]
for i in range(N):
    vel = v[i]
    time = t[i]
    for _ in range(time):
        a.append(a[-1] + vel)

for i in range(M):
    vel = v2[i]
    time = t2[i]
    for _ in range(time):
        b.append(b[-1] + vel)

first = ''
count = 0
for t in range(1,len(a)):
    if a[t] > b[t]:
        if first != 'a':
            count += 1
            first = 'a'
    elif a[t] < b[t]:
        if first != 'b':
            count += 1
            first = 'b'
    else:
        if first != 'ab':
            count += 1
            first ='ab'

print(count )