n,k = map(int,input().split())
bombs = [int(input()) for _ in range(n)]

max_num = -1
for i in range(n):
    for j in range(i+1,n):
        if bombs[i] == bombs[j] and j-i <= k:
            max_num = max(max_num,bombs[i])

print(max_num)