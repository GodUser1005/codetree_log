n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

a = [0]
b = [0]

for i in range(len(t)):
    vi = v[i]
    ti = t[i]
    for _ in range(ti):
        a.append(a[-1] + vi)

for i in range(len(t2)):
    vi = v2[i]
    ti = t2[i]
    for _ in range(ti):
        b.append(b[-1] + vi)

first = ''
count = -1

for t in range(1,len(a)):
    if a[t] > b[t] and first != 'a':
        count += 1
        first = 'a'
    elif a[t] < b[t] and first != 'b':
        count += 1
        first = 'b'

print(count)

