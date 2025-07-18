x,y = map(int,input().split())
max_sum = 0
for i in range(x,y+1):
    sum = 0
    num = i
    for j in range(4,-1,-1):
        sum += num // (10**j)
        num %= (10**j)
    max_sum = max(sum,max_sum)
print(max_sum)