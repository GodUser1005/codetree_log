dirs = input()

# Please write your code here.
dx = [0,1,0,-1]
dy = [1,0,-1,0]

pos = [0,0]
look_at_index = 0

for dir in dirs:
    if dir == 'L':
        look_at_index = (look_at_index + 3) % 4
    elif dir == 'R':
        look_at_index = (look_at_index + 1) % 4
    elif dir == 'F':
        pos[0] += dx[look_at_index]
        pos[1] += dy[look_at_index]

print(pos[0],pos[1])