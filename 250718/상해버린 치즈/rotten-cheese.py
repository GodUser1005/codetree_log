n,m,d,s = map(int,input().split())
cheese_time_list = [tuple(map(int,input().split())) for _ in range(d)]
sick_time_list = [tuple(map(int,input().split())) for _ in range(s)]

decay_prob = [0] * (m + 1)
cheese_eat_check = [[0] * (m+1) for _ in range(n+1)]

for i in range(s):
    for j in range(d):
        if sick_time_list[i][0] == cheese_time_list[j][0]:
            if sick_time_list[i][1] > cheese_time_list[j][2] and cheese_eat_check[cheese_time_list[j][0]][cheese_time_list[j][1]] == 0:
                decay_prob[cheese_time_list[j][1]] += 1
                cheese_eat_check[cheese_time_list[j][0]][cheese_time_list[j][1]] = 1

sick_prob = [0] * (n+1)
for i in range(1,m+1):
    if decay_prob[i] == s:
        for j in range(d):
            if cheese_time_list[j][1] == i:
                sick_prob[cheese_time_list[j][0]] = 1

print(sum(sick_prob))

