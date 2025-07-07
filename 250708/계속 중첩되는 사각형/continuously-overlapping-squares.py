n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
offset = 100
mat = [[0] * (2*offset +1) for _ in range(2*offset+1)]

for i in range(n):
    for j in range(y1[i],y2[i]):
        for k in range(x1[i],x2[i]):
            if i % 2 == 0:
                mat[j][k] = 1
            else:
                mat[j][k] = 2

s = 0
for j in range(y1[i],y2[i]):
    for k in range(x1[i],x2[i]):
        if mat[j][k] == 2:
            s += 1
print(s)