n,b = map(int,input().split())
p = [int(input()) for _ in range(n)]

max_count = 0

for i in range(n):
    temp = p[:]
    temp[i] //= 2
    temp.sort()
    count = 0
    temp_b = b
    for j in range(n):
        temp_b -= temp[j]
        if temp_b >= 0:
            count += 1
        else:
            break
    max_count = max(max_count,count)

print(max_count)