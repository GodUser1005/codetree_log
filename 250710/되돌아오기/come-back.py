n = int(input())
directions = []
distances = []
for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)
    directions.append(direction)
    distances.append(distance)

pos = [0,0]

def move(direction):
    directions = {'W':(0,-1),'S':(1,0),'N':(-1,0),'E':(0,1)}
    pos[0] += directions[direction][0]
    pos[1] += directions[direction][1]

time = 0

for i in range(n):
    direction = directions[i]
    distance = distances[i]
    for _ in range(distance):
        move(direction)
        time += 1
        if pos == [0,0]:
            break
    if pos == [0,0]:
        break
print(time)




