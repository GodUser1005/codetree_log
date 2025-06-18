n,m = map(int,input().split())

mat = [[0]*n for _ in range(n)]
cnt = 1

for i in range(1,m+1):
    r,c = map(int,input().split())
    r,c = r-1,c-1
    mat[r][c] = i

for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()