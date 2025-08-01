n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
x1,x2 = zip(*segments)

min_x1 = 100
min_x1_id = 0
max_x2 = 0
max_x2_id = 100
for i in range(n):
    if min_x1 > x1[i]:
        min_x1 = x1[i]
        min_x1_id = i
    if max_x2 < x2[i]:
        max_x2 = x2[i]
        max_x2_id = i

min_x1 = 100
max_x2 = 0
for i in range(n):
    if i == min_x1_id:
        continue
    if min_x1 > x1[i]:
        min_x1 = x1[i]
    if max_x2 < x2[i]:
        max_x2 = x2[i]
ans = max_x2 - min_x1

min_x1 = 100
max_x2 = 0
for i in range(n):
    if i == max_x2_id:
        continue
    if min_x1 > x1[i]:
        min_x1 = x1[i]
    if max_x2 < x2[i]:
        max_x2 = x2[i]

ans = min(ans,max_x2 - min_x1)

print(ans)

