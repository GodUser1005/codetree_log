n,m = map(int,input().split())

mat = [[0] * (m+2) for _ in range(n+2)]

directions = [(0,1),(1,0),(0,-1),(-1,0)]
d_i = 0
r,c = 1,1

for i in range(n*m):
    mat[r][c] = chr(ord('A') + (i % 26))
    next_r, next_c = r + directions[d_i][0], c + directions[d_i][1]
    if 0 < next_r < n+1 and 0 < next_c < m+1 and mat[next_r][next_c] == 0:
        r,c = next_r,next_c
    else:
        d_i = (d_i + 1) % 4
        r,c =  r + directions[d_i][0], c + directions[d_i][1]

for row in mat[1:-1]:
    for e in row[1:-1]:
        print(e,end=" ")
    print()