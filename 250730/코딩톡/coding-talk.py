n,m,p = map(int,input().split())
logs = []
for _ in range(m):
    c,u = input().split()
    u = int(u)
    logs.append((c,u))

checks = [0] * n
for c,u in logs[p-1:]:
    checks[ord(c)-ord('A')] = 1

for i in range(n):
    if checks[i] == 0:
        print(chr(ord('A') + i),end=" ")
