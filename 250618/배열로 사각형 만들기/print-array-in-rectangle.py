mat = [[0] * 5 for _ in range(5)]
for i in range(5):
    mat[i][0], mat[0][i] = 1,1

for i in range(1,5):
    for j in range(1,5):
        mat[i][j] = mat[i-1][j] + mat[i][j-1]

for i in range(5):
    for j in range(5):
        print(mat[i][j],end=" ")
    print()
