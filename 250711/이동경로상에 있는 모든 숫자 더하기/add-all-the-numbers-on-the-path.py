n,t = map(int,input().split())
queries = input()
mat = [list(map(int,input().split())) for _ in range(n)]

r = c = n // 2
directions = [(-1,0),(0,1),(1,0),(0,-1)]
d_i = 0
ans = mat[r][c]

def rotate(d):
    global d_i
    if d == 'L':
        d_i = (d_i + 3) % 4
    else:
        d_i = (d_i + 1) % 4

def in_range(r,c):
    return 0 <= r < n and 0 <= c < n

def move():
    global r,c,ans
    next_r, next_c = r + directions[d_i][0], c + directions[d_i][1]
    if in_range(next_r,next_c):
        r,c = next_r,next_c
        ans += mat[r][c]

for q in queries:
    if q == 'F':
        move()
    else:
        rotate(q)

print(ans)


