n = int(input())
a = [0] + list(map(int, input().split()))

# Please write your code here.
min_num = min(a[1:])

count = 0
second_min = 100
ans = 100
for i in range(1,n+1):
    if a[i] > min_num:
        second_min = min(second_min,a[i])

for i,num in enumerate(a[1:]):
    if num == second_min:
        count += 1
        ans = i+1

if count == 1:
    print(ans)
else:
    print(-1)
    
