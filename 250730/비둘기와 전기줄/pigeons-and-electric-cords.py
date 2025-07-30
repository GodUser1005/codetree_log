counts = [0] * 11
birds = [-1] * 11

n = int(input())

for _ in range(n):
    b,p = map(int,input().split())
    if birds[b] == -1:
        birds[b] = p
    elif birds[b] != p:
        counts[b] += 1
        birds[b] = p

print(sum(counts))