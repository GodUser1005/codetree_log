n,m = map(int,input().split())
seq = list(map(int,input().split()))

def cal_num(s_pos,m):
    sum = 0
    for _ in range(m):
        sum += seq[s_pos-1]
        s_pos = seq[s_pos-1]
    return sum

max_sum = 0
for i in range(n):
    max_sum = max(max_sum,cal_num(i,m))

print(max_sum)