n, m = map(int, input().split())

# Please write your code here.
mat = [[0]*m for _ in range(n)]
cnt = 1

for i in range(n+m-1):
    for j in range(i+1):
        if j >= n or i-j >= m:
            continue
        mat[j][i-j] = cnt
        cnt += 1
    
for i in range(n):
    for j in range(m):
        print(mat[i][j],end=" ")
    print()
    
        
