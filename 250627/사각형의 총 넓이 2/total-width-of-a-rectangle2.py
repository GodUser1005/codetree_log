n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
mat = [[0] * 201 for _ in range(201)]
offset = 100

for i in range(n):
    for j in range(x1[i],x2[i]):
        for k in range(y1[i],y2[i]):
            mat[j][k] = 1
    
cnt = 0
for row in mat:
    for e in row:
        if e == 1:
            cnt += 1
print(cnt)