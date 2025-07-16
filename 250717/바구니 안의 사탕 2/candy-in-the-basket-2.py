n,k = map(int,input().split())
line = [0] * 101

for _ in range(n):
    c,b = map(int,input().split())
    line[b] += c

max_count = 0
for i in range(101):
    count = 0
    for j in range(i-k,i+k+1):
        if j >= 0 and j < 101:
            count += line[j]
    max_count = max(count,max_count)
        

print(max_count)

