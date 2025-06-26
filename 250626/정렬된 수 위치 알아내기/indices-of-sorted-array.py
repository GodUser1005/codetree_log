n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
nums = [(i+1,sequence[i]) for i in range(n)]
nums.sort(key=lambda x: (x[1],x[0]))
pos = [0]*(n+1)
for rank in range(n):
    pos[nums[rank][0]] = rank+1

for p in pos[1:]:
    print(p,end=" ")