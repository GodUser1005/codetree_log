a, b = map(int, input().split())
n = map(int,list(input()))

# Please write your code here.
def n_digit_to_dec(n,a):
    num = 0
    for digit in n:
        num = num*a + digit
    return num

def dec_to_n_digit(n,b):
    digits = []
    while n >= b:
        digits.append(n % b)
        n //= b
    digits.append(n)
    digits = digits[::-1]
    return int("".join([str(digit) for digit in digits]))

print(dec_to_n_digit(n_digit_to_dec(n,a),b))