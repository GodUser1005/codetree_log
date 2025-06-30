x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

offset = 1000
mat = [[0]*(offset*2+1) for _ in range(offset *2 + 1)]

def paint(x1,y1,x2,y2,p):
    for i in range(y1,y2):
        for j in range(x1,x2):
            mat[i][j] = p

paint(x1[0]+offset,y1[0]+offset,x2[0]+offset,y2[0]+offset,1)
paint(x1[1]+offset,y1[1]+offset,x2[1]+offset,y2[1]+offset,1)
paint(x1[2]+offset,y1[2]+offset,x2[2]+offset,y2[2]+offset,2)

cnt = 0
for row in mat:
    for e in row:
        if e == 1:
            cnt += 1

print(cnt)
