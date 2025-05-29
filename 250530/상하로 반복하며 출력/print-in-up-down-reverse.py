n = int(input())
matrix = [[0]*n for _ in range(n)]
for col in range(n):
    start,end,step = 0,0,0
    count = 1
    if col % 2 == 0:
        start,end,step = 0,n,1
    else:
        start,end,step = n-1,-1,-1
    for row in range(start,end,step):
        matrix[row][col] = count
        count += 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end="")
    print()