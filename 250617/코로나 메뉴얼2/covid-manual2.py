count = [0,0,0,0]
for _ in range(3):
    c,t = input().split()
    t = int(t)
    if c == 'Y':
        if t >= 37:
            count[0] += 1
        else:
            count[2] += 1
    else:
        if t >= 37:
            count[1] += 1
        else:
            count[3] += 1

for c in count:
    print(c,end=" ")

if count[0] >= 2:
    print('E')