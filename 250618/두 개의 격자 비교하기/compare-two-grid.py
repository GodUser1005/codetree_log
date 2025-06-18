n,m = map(int,input().split())

mat_1 = [list(map(int,input().split())) for _ in range(n)]
mat_2 = [list(map(int,input().split())) for _ in range(n)]

result = [[0 if mat_1[i][j] == mat_2[i][j] else 1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(result[i][j],end=" ")
    print()