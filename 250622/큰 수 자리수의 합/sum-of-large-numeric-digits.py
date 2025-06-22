def digit_sum(n):
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)

a, b, c = map(int, input().split())

# Please write your code here.
print(digit_sum(a*b*c))