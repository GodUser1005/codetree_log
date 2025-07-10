n = int(input())
mat = [[0] * (n+2) for _ in range(n+2)]

for i in range(1,n+1):
    mirrors = input()
    for j in range(1,n+1):
        mat[i][j] = mirrors[j-1]
directions = [(1,0),(0,-1),(-1,0),(0,1)]

def initiate(k):
    q,r = (k-1) // n, (k-1) % n
    if q == 0:
        return [0,r+1], 0
    elif q == 1:
        return [r+1,n+1], 1
    elif q == 2:
        return [n+1,n+1 - (r+1)], 2
    elif q == 3:
        return [n+1 - (r+1),0], 3

def reflect(d_i,mirror):
    if mirror == '/':
        if directions[d_i][0] == 0:
            return (d_i + 3) % 4
        else:
            return (d_i + 1) % 4
    else:
        if directions[d_i][0] == 0:
            return (d_i + 1) % 4
        else:
            return (d_i + 3) % 4

def move(d_i):
    pos[0] += directions[d_i][0]
    pos[1] += directions[d_i][1]

k = int(input())
pos,d_i = initiate(k)

cnt = 0
while True:
    move(d_i)
    mirror = mat[pos[0]][pos[1]]
    if mirror != 0:
        cnt += 1
        d_i = reflect(d_i,mirror)
    else:
        break

print(cnt)

# for row in mat:
#     for e in row:
#         print(e,end=" ")
#     print()
