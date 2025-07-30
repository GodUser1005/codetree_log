counts = [0] * 11
birds = [-1] * 11

n = int(input())

for _ in range(n):
    b,p = map(int,input().split())
    if (birds[b] == 0 and p == 1) or (birds[b] == 1 and p == 0):
        counts[b] += 1
    birds[b] = p

print(sum(counts))