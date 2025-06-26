n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
nums_reverse = nums[::-1]
print(max([nums[i]+nums_reverse[i] for i in range(n)]))
