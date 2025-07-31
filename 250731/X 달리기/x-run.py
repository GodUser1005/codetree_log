x = int(input())

# Please write your code here.
def cal_max_v(x):
    max_v = 1
    while True:
        dist = 0
        for i in range(1,max_v+1):
            dist += i
        dist = 2*dist - max_v
        if dist > x:
            return max_v - 1
        max_v += 1

max_v = cal_max_v(x)
print((2 * max_v - 1) + 1)
            
        