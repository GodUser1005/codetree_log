n = int(input())
mat = [[0]*(n+2) for _ in range(n+2)]

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        mat[i+1][j+1] = row[j]

# Please write your code here.
directions = [(1,0),(0,1),(-1,0),(0,-1)]

def is_right(row,column):
    cnt = 0
    for d_r,d_c in directions:
        if mat[row+d_r][column+d_c] == 1:
            cnt += 1
    if cnt >= 3:
        return True
    return

ans = 0
for r in range(1,n+1):
    for c in range(1,n+1):
        if is_right(r,c):
            ans += 1

print(ans)

