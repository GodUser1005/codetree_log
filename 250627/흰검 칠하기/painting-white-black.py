n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
offset = 100000
pos = offset
tile = [0] * 200001
b_count = [0] * 200001
w_count = [0] * 200001

def paint(x,d):
    global pos
    shift = 1 if d == 'R' else -1
    for _ in range(x):
        if d == 'R':
            tile[pos] = 'B'
            b_count[pos] += 1
        elif d == 'L':
            tile[pos] = 'W'
            w_count[pos] += 1
        pos += shift
    pos -= shift

def paint_gray():
    for i in range(len(tile)):
        if b_count[i] >= 2 and w_count[i] >= 2:
            tile[i] = 'G'

def count_color():
    count = [0,0,0]
    for t in tile:
        if t == 'W':
            count[0] += 1
        elif t == 'B':
            count[1] += 1
        elif t == 'G':
            count[2] += 1

    return count

for i in range(n):
    x,d = commands[i]
    x = int(x)
    paint(x,d)

paint_gray()
for count in count_color():
    print(count,end=" ")
    


