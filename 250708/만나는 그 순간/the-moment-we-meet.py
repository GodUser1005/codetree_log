n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
a = [0]
b = [0]

for i in range(n):
    direct = d[i]
    time = t[i]
    for _ in range(time):
        if direct == 'R':
            a.append(a[-1] + 1)
        else:
            a.append(a[-1] - 1)

for i in range(m):
    direct = d2[i]
    time = t2[i]
    for _ in range(time):
        if direct == 'R':
            b.append(b[-1] + 1)
        else:
            b.append(b[-1] - 1)

answer = -1

for i in range(1,len(a)):
    if a[i] == b[i]:
        answer = i
        break
print(answer)



