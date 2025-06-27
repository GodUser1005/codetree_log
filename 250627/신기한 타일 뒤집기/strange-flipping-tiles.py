n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
MAX_N = 100000
tiles = ['G'] * (2*MAX_N + 1)
pos = MAX_N

def filp_tile(x,d):
    global pos
    if d == 'L':
        for _ in range(x):
            tiles[pos] = 'W'
            pos -= 1
        pos += 1
    elif d == 'R':
        for _ in range(x):
            tiles[pos] = 'B'
            pos += 1
        pos -= 1

def count():
    b,w = 0,0
    for color in tiles:
        if color == 'B':
            b += 1
        elif color == 'W':
            w += 1
    return w,b

for i in range(n):
    filp_tile(x[i],dir[i])

for c in count():
    print(c,end=" ")
