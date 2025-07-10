n = int(input())
directions = []
distances = []
for _ in range(n):
    dir, dis = input().split()
    if dir == 'W':
        dir = 0
    elif dir == 'S':
        dir = 1
    elif dir == 'N':
        dir = 2
    else:
        dir = 3
    directions.append(dir)
    distances.append(int(dis))

# Please write your code here.

wsne = [(-1,0),(0,-1),(0,1),(1,0)]
pos = [0,0]

for i in range(n):
    pos[0],pos[1] = pos[0]+wsne[directions[i]][0]*distances[i],pos[1]+wsne[directions[i]][1]*distances[i]

print(pos[0],pos[1])


    
