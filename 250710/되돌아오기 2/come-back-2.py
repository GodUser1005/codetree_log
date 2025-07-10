commands = input()

pos = [0,0]
direction = 0

directions = [(-1,0),(0,1),(1,0),(0,-1)]

def rotate(d):
    global direction
    if d == 'L':
        direction = (direction + 3) % 4
    else:
        direction = (direction + 1) % 4

# Please write your code here.
time = -1

for i in range(len(commands)):
    if commands[i] == 'F':
        pos[0] += directions[direction][0]
        pos[1] += directions[direction][1]
        if pos == [0,0]:
            time = i+1
            break
    else:
        rotate(commands[i])

print(time)

