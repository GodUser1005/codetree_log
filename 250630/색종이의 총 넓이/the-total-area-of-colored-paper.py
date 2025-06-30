n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

offset = 100
mat = [[0]*(offset*2+1) for _ in range(offset*2+1)]

def paint_square(x,y):
    for i in range(y,y+8):
        for j in range(x,x+8):
            mat[i][j] = 1

for i in range(n):
    paint_square(x[i] + offset, y[i] + offset)


cnt = 0
for row in mat:
    for e in row:
        if e == 1:
            cnt += 1

print(cnt)