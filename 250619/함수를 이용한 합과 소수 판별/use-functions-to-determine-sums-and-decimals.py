def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_even(n):
    s = str(n)
    sum_ = sum(map(int,s))
    if sum_ % 2 == 0:
        return True
    return False


a, b = map(int, input().split())

# Please write your code here.
cnt = 0
for i in range(a,b+1):
    if is_even(i) and is_prime(i):
        cnt += 1

print(cnt)