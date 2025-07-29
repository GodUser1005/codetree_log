n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

ans = 'No'
for i in range(n):
    x1,x2 = 1,100
    for j in range(n):
        if i == j:
            continue
        y1,y2 = segments[j]
        if x1 <= y1 <= x2 or y1 <= x1 <= y2:
            tmp = [x1,x2,y1,y2]
            tmp.sort()
            x1,x2 = tmp[1],tmp[2]
        else:
            x1 = 0
            break
    if x1 > 0:
        ans = 'Yes'
        break

print(ans)
        