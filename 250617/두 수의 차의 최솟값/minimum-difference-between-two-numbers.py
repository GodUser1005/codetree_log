n = int(input())
arr = list(map(int,input().split()))
min_ = 100
for i in range(1,len(arr)):
    diff = arr[i] - arr[i-1]
    if min_ > diff:
        min_ = diff

print(min_)