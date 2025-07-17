n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.

count = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            first_diff = abs(a1-i)
            second_diff = abs(b1-j)
            third_diff = abs(c1-k)
            if (first_diff <= 2 or first_diff >= n-2) and (second_diff <= 2 or second_diff >= n-2) and (third_diff <= 2 or third_diff >= n-2):
                count += 1
                continue
            first_diff = abs(a2-i)
            second_diff = abs(b2-j)
            third_diff = abs(c2-k)
            if (first_diff <= 2 or first_diff >= n-2) and (second_diff <= 2 or second_diff >= n-2) and (third_diff <= 2 or third_diff >= n-2):
                count += 1
print(count)