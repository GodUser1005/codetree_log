k,n = map(int,input().split())
rank = [list(map(int,input().split())) for _ in range(k)]

count = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a != b:
            satisfied = True
            for i in range(k):
                rank_a = 0
                rank_b = 0
                for j in range(n):
                    if rank[i][j] == a:
                        rank_a = j
                    elif rank[i][j] == b:
                        rank_b = j
                if rank_a > rank_b:
                    satisfied = False
                    break
            if satisfied:
                count += 1
print(count)
                