ability = list(map(int, input().split()))

# Please write your code here.
ability.sort()
t = []
t.append(ability[0]+ability[5])
t.append(ability[1]+ability[4])
t.append(ability[2]+ability[3])

print(max(t)-min(t))