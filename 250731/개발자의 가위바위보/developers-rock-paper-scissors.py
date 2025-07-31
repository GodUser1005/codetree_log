n = int(input())
logs = [tuple(map(int,input().split())) for _ in range(n)]

count_win = 0
count_draw = 0
for a,b in logs:
    if a == b:
        count_draw += 1
    elif a == 3 and b == 1:
        count_win += 1
    elif b > a and b-a == 1:
        count_win += 1

count_win = max(count_win,n - count_draw - count_win)
print(count_win)
    
    