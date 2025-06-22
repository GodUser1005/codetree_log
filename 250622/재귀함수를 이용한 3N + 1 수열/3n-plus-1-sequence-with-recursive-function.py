def until_1(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + until_1(n//2)
    else:
        return 1 + until_1(3*n + 1)

n = int(input())

# Please write your code here.

print(until_1(n))