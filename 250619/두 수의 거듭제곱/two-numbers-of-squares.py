def a_square_b(a,b):
    result = 1
    for _ in range(b):
        result *= a
    return result


a, b = map(int, input().split())

# Please write your code here.

print(a_square_b(a,b))