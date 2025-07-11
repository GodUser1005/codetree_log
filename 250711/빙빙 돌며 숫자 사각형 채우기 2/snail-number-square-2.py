n,m = map(int,input().split())

mat = [[0] * (m+2) for _ in range(n+2)]
directions = [(1,0),(0,1),(-1,0),(0,-1)]

d_i = 0
r,c = 1,1

for i in range(1,n*m + 1):
    mat[r][c] = i
    next_r = r + directions[d_i][0]
    next_c = c + directions[d_i][1]
    if (0 < next_r <= n and 0 < next_c <= m) and mat[next_r][next_c] == 0:
        r,c = next_r,next_c
    else:
        d_i = (d_i + 1) % 4
        r,c = r + directions[d_i][0], c+directions[d_i][1]

for row in mat[1:-1]:
    for e in row[1:-1]:
        print(e,end=" ")
    print()
        
    