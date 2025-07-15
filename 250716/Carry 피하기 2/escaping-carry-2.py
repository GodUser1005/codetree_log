import sys
MIN_INT = -sys.maxsize

n = int(input())
nums = [int(input()) for _ in range(n)]

def occur_carry(n1,n2):
    str1 = str(n1)
    str2 = str(n2)
    for i in range(-1,-min(len(str1),len(str2))-1,-1):
        if int(str1[i]) + int(str2[i]) >= 10:
            return True
    return False

max_sum = MIN_INT

for i in range(n-2):
    num1 = nums[i]
    for j in range(i+1,n-1):
        num2 = nums[j]
        if not occur_carry(num1,num2):
            for k in range(j+1,n):
                num3 = nums[k]
                if not occur_carry(num1+num2,num3):
                    max_sum = max(max_sum,num1+num2+num3)

print(max_sum if max_sum >= 0 else -1)
    




