n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
directions = [(0,1),(-1,0),(0,-1),(1,0)]
r = c = n // 2

def move(d_i):
    global r,c
    r = r + directions[d_i][0]
    c = c + directions[d_i][1]

def paint():
    count = 1
    d_i = 0
    for i in range(1,n+1):
        for _ in range(2):
            for _ in range(i):
                grid[r][c] = count
                count += 1
                move(d_i)
                if (r < 0 or r >= n) or (c < 0 or c >= n):
                    return
            d_i = (d_i + 1) % 4

paint()

for row in grid:
    for e in row:
        print(e,end=" ")
    print()




