n = int(input())
nums = []
c1s = []
c2s = []
for _ in range(n):
    num,c1,c2 = input().split()
    c1,c2 = int(c1),int(c2)
    num = list(map(int,num))
    nums.append(num)
    c1s.append(c1)
    c2s.append(c2)

pred = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i == j or i == k or j == k:
                continue
            satisfied = True
            for m in range(n):
                c1,c2 = 0,0
                if nums[m][0] == i:
                    c1 += 1
                elif i in nums[m]:
                    c2 += 1
                
                if nums[m][1] == j:
                    c1 += 1
                elif j in nums[m]:
                    c2 += 1
                
                if nums[m][2] == k:
                    c1 += 1
                elif k in nums[m]:
                    c2 += 1

                if not (c1 == c1s[m] and c2 == c2s[m]):
                    satisfied = False
                    break
            if satisfied:
                pred.append(i*100+j*10+k)

print(len(pred))
                


