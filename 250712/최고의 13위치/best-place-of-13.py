n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]

max_cnt = 0
for i in range(n):
    for j in range(n-2):
        cnt = 0
        for e in mat[i][j:j+3]:
            if e == 1:
                cnt += 1
        
        max_cnt = max(cnt,max_cnt)

print(max_cnt)