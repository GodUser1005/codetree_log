n = int(input())
seats = list(input())

# Please write your code here.
max_near = 0
for i in range(n):
    if seats[i] == '1':
        continue
    tmp = seats.copy()
    tmp[i] = '1'
    positions = [j for j in range(n) if tmp[j] == '1']
    min_dist = 1000
    for j in range(len(positions)):
        for k in range(j+1,len(positions)):
            dist = positions[k] - positions[j]
            min_dist = min(dist,min_dist)
    max_near = max(max_near,min_dist)

print(max_near)

    