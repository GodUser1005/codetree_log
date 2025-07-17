n = int(input())
x_list = []
y_list = []
for _ in range(n):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

min_s = 40000*40000

for i in range(n):
    min_x,min_y = 40000,40000
    max_x,max_y = 0,0
    for j in range(n):
        if i == j:
            continue
        min_x = min(x_list[j],min_x)
        min_y = min(y_list[j],min_y)
        max_x = max(x_list[j],max_x)
        max_y = max(y_list[j],max_y)
    s = (max_x-min_x) * (max_y-min_y)
    min_s = min(s,min_s)

print(min_s)


    