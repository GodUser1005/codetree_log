def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())

# Please write your code here.
arr = [n for n in range(a,b+1) if is_prime(n)]

print(sum(arr))