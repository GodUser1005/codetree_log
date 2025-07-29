n = int(input())
segments = [tuple(map(int,input().split())) for _ in range(n)]

x1,x2 = segments[0]

ans = 'Yes'
for y1,y2 in segments[1:]:
    if x1 <= y1 <= x2 or y1 <= x1 <= y2:
        tmp = [x1,x2,y1,y2]
        tmp.sort()
        x1,x2 = tmp[1],tmp[2]
    else:
        ans = 'No'
        break

print(ans)