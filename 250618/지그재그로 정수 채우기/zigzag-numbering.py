n, m = map(int, input().split())

# Please write your code here.
mat = [[0]*m for _ in range(n)]
cnt = 0

for j in range(m):
    for i in range(n):
        if j % 2 == 0:
            mat[i][j] = cnt
        else:
            mat[n-1 - i][j] = cnt
        cnt += 1

for i in range(n):
    for j in range(m):
        print(mat[i][j],end=" ")
    print()