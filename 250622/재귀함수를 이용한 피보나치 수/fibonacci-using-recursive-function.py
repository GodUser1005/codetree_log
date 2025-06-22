def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


N = int(input())

# Please write your code here.
print(fibonacci(N))