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
dist = sum(range(1,max_v+1))*2 - max_v
ans = (2 * max_v - 1)
if dist < x:
    ans += 1
    
print(ans)
            
        