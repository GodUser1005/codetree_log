n = int(input())

# Please write your code here.
def decimal_to_digit(n):
    digit = []
    while n > 2:
        digit.append(str(n % 2))
        n //= 2
        if n < 2:
            digit.append(str(n))
    digit = digit[::-1]
    return "".join(digit)

print(decimal_to_digit(n))