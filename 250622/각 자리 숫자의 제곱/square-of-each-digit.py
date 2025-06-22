def square_sum(n):
    if n < 10:
        return n**2
    return (n % 10)**2 + square_sum(n // 10)


N = int(input())

# Please write your code here.
print(square_sum(N))