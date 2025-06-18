n,m = map(int,input().split())
mat = [[0]*m for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(m):
        mat[i][j] = cnt
        cnt += 1

for i in range(n):
    for j in range(m):
        print(mat[i][j],end=" ")
    print()
