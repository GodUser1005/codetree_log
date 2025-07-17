import sys
MAX_INT = sys.maxsize

abilities = list(map(int, input().split()))

# Please write your code here.

total_abilities = sum(abilities)

min_diff = MAX_INT
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            team_a = abilities[i] + abilities[j] + abilities[k]
            team_b = total_abilities-team_a
            dif = abs(team_a-team_b)
            min_diff = min(min_diff,dif)

print(min_diff)

