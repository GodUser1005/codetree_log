N = input()

# Please write your code here.
def bin_to_dec(n):
    result = 0
    for bit in n:
        result *= 2
        if bit == '1':
            result += 1
    return result

def dec_to_bin(n):
    digit = []
    while n >= 2:
        digit.append(n % 2)
        n //= 2
    digit.append(n)
    return "".join([str(bit) for bit in digit[::-1]])

print(dec_to_bin((bin_to_dec(N)*17)))