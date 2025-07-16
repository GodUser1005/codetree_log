n,k = map(int,input().split())
line = [0] * 101

for _ in range(n):
    c,b = map(int,input().split())
    line[b] += c

def count_candy(arr):
    return sum(arr)

max_count = 0
for c in range(k,100-k+1):
    count = count_candy(line[c-k:c+k+1])
    max_count = max(count,max_count)

print(max_count)

