nums = list(map(int,input().split()))
s = sum(nums)
a = s//len(nums)
r = s-a
print(s,a,r,sep="\n")