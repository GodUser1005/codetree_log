n,m = map(int,input().split())

mat = [[0] * (n+2) for _ in range(n+2)]

def is_relax(r,c):
    cnt = 0
    if mat[r-1][c] == 1:
        cnt += 1
    if mat[r+1][c] == 1:
        cnt += 1
    if mat[r][c-1] == 1:
        cnt += 1
    if mat[r][c+1] == 1:
        cnt += 1
    
    return cnt == 3

def paint(r,c):
    mat[r][c] = 1

for _ in range(m):
    r,c = map(int,input().split())
    paint(r,c)
    ans = 1 if is_relax(r,c) else 0
    print(ans)