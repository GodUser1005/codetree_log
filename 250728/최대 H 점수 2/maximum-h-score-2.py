n,l = map(int,input().split())
arr = list(map(int,input().split()))
counts = [0] * 101
for i in arr:
    counts[i] += 1


def cal_h():
    for i in range(1,n+1):
        cnt = 0
        for j in range(n):
            if arr[j] >= i:
                cnt += 1
        if cnt < i:
            return i-1
    return n

cur_h = cal_h()

if counts[cur_h+1] <= l:
    print(cur_h + 1)
else:
    print(cur_h)
