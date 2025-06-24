n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for e in nums:
    print(e,end=" ")
print()
for e in nums[::-1]:
    print(e,end=" ")