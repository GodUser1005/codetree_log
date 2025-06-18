n,m = map(int,input().split())

mat = [[0]*n for _ in range(n)]

for _ in range(m):
    r,c = map(int,input().split())
    v = r*c
    r,c = r-1,c-1
    mat[r][c] = v

for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()