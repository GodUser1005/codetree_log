n = int(input())
cnt = 1

mat = [[0]*n for _ in range(n)]

for j in range(n):
    for i in range(n):
        if (n-1 - j) % 2 == (n-1) % 2:
            mat[n-1 - i][n-1 - j] = cnt
        else:
            mat[i][n-1 - j] = cnt
        cnt += 1

for row in mat:
    for element in row:
        print(element,end=" ")
    print()