def switch_direction(d):
    if d == 'D':
        return 'U'
    elif d == 'U':
        return 'D'
    elif d == 'R':
        return 'L'
    elif d == 'L':
        return 'R'

n,t = map(int,input().split())
r,c,d = input().split()
r,c = map(int,(r,c))

directions = {
    'U':(1,0),
    'D':(-1,0),
    'R':(0,1),
    'L':(0,-1)
}

for _ in range(t):
    tmp = [r,c]
    tmp[0] += directions[d][0]
    tmp[1] += directions[d][1]
    if (1 <= tmp[0] <= n) and (1 <= tmp[1] <= n):
        r,c = tmp
    else:
        d = switch_direction(d)
    # print(r,c,d )

print(r,c)

    
