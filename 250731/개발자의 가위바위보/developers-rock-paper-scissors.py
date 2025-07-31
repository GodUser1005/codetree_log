n = int(input())
logs = [tuple(map(int,input().split())) for _ in range(n)]

count_1 = 0
count_2 = 0
for a,b in logs:
    if a == 3 and b == 1:
        count_1 += 1
    elif b > a:
        count_1 += 1
    
    if b == 3 and a == 1:
        count_2 += 1
    elif a > b:
        count_2 += 1

print(max(count_1,count_2))