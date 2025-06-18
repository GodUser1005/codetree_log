n = int(input())
cnt = 1

mat = [[0]*n for _ in range(n)]

for j in range(-1,(-1)*(n+1),-1):
    for i in range(n):
        if j % 2 == 0:
            mat[i][j] = cnt
        else:
            mat[n-1 - i][j] = cnt
        cnt += 1

for row in mat:
    for element in row:
        print(element,end=" ")
    print()