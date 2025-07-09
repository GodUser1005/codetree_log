n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
a = [0]
b = [0]

for i in range(n):
    time, direction = t[i], d[i]
    for _ in range(time):
        if direction == 'L':
            a.append(a[-1]-1)
        else:
            a.append(a[-1]+1)

for i in range(m):
    time, direction = t_b[i], d_b[i]
    for _ in range(time):
        if direction == 'L':
            b.append(b[-1]-1)
        else:
            b.append(b[-1]+1)

if len(a) > len(b):
    for _ in range(len(a)-len(b)):
        b.append(b[-1])
else:
    for _ in range(len(b)-len(a)):
        a.append(a[-1])

count = 0
for i in range(1,len(a)):
    if a[i] == b[i] and a[i-1] != b[i-1]:
        count += 1
print(count)
# print(a)
# print(b)

    


