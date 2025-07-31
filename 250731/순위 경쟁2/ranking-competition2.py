prev = 'AB'
score_a = 0
score_b = 0

n = int(input())
logs = []
for i in range(n):
    p,s = input().split()
    s = int(s)
    logs.append((p,s))

count = 0
for p,s in logs:
    if p == 'A':
        score_a += s
    else:
        score_b += s
    
    honor = 0
    if score_a > score_b:
        honor = 'A'
    elif score_b > score_a:
        honor = 'B'
    else:
        honor = 'AB'
    
    if prev != honor:
        count += 1
        prev = honor

print(count)