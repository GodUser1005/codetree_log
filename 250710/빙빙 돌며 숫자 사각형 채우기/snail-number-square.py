n,m = map(int,input().split())

mat = [[0]*m for _ in range(n)]
r,c = 0,0
directions = [(0,1),(1,0),(0,-1),(-1,0)]
d_i = 0

def rotate():
    global d_i
    d_i = (d_i + 1) % 4

def is_ok_to_go():
    next_step = r + directions[d_i][0], c + directions[d_i][1]
    if (0 <= next_step[0] < n and 0 <= next_step[1] < m) and (mat[next_step[0]][next_step[1]] == 0):
        return True
    return False

for i in range(1,n*m+1):
    mat[r][c] = i
    if is_ok_to_go():
        r,c = r + directions[d_i][0], c + directions[d_i][1]
    else:
        rotate()
        r,c = r + directions[d_i][0], c + directions[d_i][1]

for row in mat:
    for e in row:
        print(e,end=" ")
    print()


