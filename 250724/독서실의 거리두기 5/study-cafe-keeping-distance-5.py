n = int(input())
state = list(map(int,input()))

def cal_near_dist(arr):
    pos_arr = [i for i in range(n) if arr[i] == 1]
    min_dist = n
    for i in range(len(pos_arr)-1):
        dist = pos_arr[i+1] - pos_arr[i]
        min_dist = min(dist,min_dist)
    return min_dist

max_near_dist = 0
for i in range(n):
    if state[i] == 0:
        tmp = state[:]
        tmp[i] = 1
        near_dist = cal_near_dist(tmp)
        max_near_dist = max(near_dist,max_near_dist)

print(max_near_dist)


