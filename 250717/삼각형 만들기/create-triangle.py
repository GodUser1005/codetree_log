n = int(input())
x_list = []
y_list = []
for _ in range(n):
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

max_s = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s = 0
            if x_list[i] == x_list[j] and y_list[i] == y_list[k]:
                s = abs(y_list[i]-y_list[j]) * abs(x_list[i]-x_list[k])
            elif x_list[i] == x_list[k] and y_list[i] == y_list[j]:
                s = abs(y_list[i]-y_list[k]) * abs(x_list[i]-x_list[j])
            elif x_list[j] == x_list[k] and y_list[j] == y_list[i]:
                s = abs(y_list[j]-y_list[k]) * abs(x_list[j]-x_list[i])
            elif x_list[j] == x_list[i] and y_list[j] == y_list[k]:
                s = abs(y_list[j]-y_list[i]) * abs(x_list[j]-x_list[k])
            elif x_list[k] == x_list[i] and y_list[k] == y_list[j]:
                s = abs(y_list[k]-y_list[i]) * abs(x_list[k]-x_list[j])
            elif x_list[k] == x_list[j] and y_list[k] == y_list[i]:
                s = abs(y_list[k]-y_list[j]) * abs(x_list[k]-x_list[i])
            max_s = max(s,max_s)

print(max_s)
