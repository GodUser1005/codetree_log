N, B = map(int, input().split())

# Please write your code here.
def dec_to_n_digit(n,b):
    n_digit = []
    while n >= b:
        n_digit.append(n % b)
        n //= b
    n_digit.append(n)
    n_digit = "".join([str(num) for num in n_digit[::-1]])
    return n_digit

print(dec_to_n_digit(N,B))