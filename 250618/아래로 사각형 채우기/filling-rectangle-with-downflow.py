n = int(input())

mat = [[0]*n for _ in range(n)]

cnt = 1
for j in range(n):
    for i in range(n):
        mat[i][j] = cnt
        cnt += 1

for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
    print()