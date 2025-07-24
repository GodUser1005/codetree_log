n = int(input())
ranges = [tuple(map(int,input().split())) for _ in range(n)]

for x in range(1,10001):
    checked = True
    v = x
    for i in range(n):
        v *= 2
        if not(ranges[i][0] <= v <= ranges[i][1]):
            checked = False
            break
    if checked:
        print(x)
        break