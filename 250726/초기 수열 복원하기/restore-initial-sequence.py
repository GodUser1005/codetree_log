n = int(input())
adjacent = list(map(int, input().split()))

# Please write your code here.

ans = []
for i in range(1,n+1):
    satisfied = True
    nums = [i]
    for sum in adjacent:
        next_num = sum - nums[-1]
        if next_num in nums:
            satisfied = False
            break
        nums.append(next_num)
    if satisfied:
        ans = nums
        break


for a in ans:
    print(a,end=" ")
