x = int(input())

# Please write your code here.
def cal_min_time(x):
    max_v = 1
    while True:
        sum_to_max_v = sum(range(1,max_v+1))
        min_dist = sum_to_max_v * 2 - max_v
        max_dist = sum_to_max_v * 2 + max_v
        if min_dist == x:
            return 2*max_v-1
        elif min_dist < x <= sum_to_max_v*2:
            return 2 * max_v
        elif x <= max_dist:
            return 2 * max_v + 1
        max_v += 1

print(cal_min_time(x))
    


            
        