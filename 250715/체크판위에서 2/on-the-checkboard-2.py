r,c = map(int,input().split())
mat =  [list(input().split()) for _ in range(r)]

start = mat[0][0]

count = 0
for i in range(1,r):
    for j in range(1,c):
        if mat[i][j] != start:
            for i2 in range(i+1,r):
                for j2 in range(j+1,c):
                    if mat[i2][j2] == start:
                        if i2 < r-1 and j2 < c-1 and mat[r-1][c-1] != start:
                            count += 1

print(count)
                        
