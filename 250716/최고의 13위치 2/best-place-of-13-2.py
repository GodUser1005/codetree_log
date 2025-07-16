import sys
MIN_INT = -sys.maxsize

n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]

max_coin = MIN_INT

for i in range(n):
    for j in range(n-2):
        for a in range(n):
            for b in range(n-2):
                if (a == i and b > j+2) or a > i:
                    coin = sum(mat[a][b:b+3]) + sum(mat[i][j:j+3])
                    max_coin = max(coin,max_coin)

print(max_coin)
