n = int(input())
cows = list(map(int,input().split()))

cnt = 0
for i,c1 in enumerate(cows):
    for j,c2 in enumerate(cows[i+1:]):
        if c1 <= c2:
            for c3 in cows[i+1:][j+1:]:
                if c2 <= c3:
                    cnt += 1

print(cnt)