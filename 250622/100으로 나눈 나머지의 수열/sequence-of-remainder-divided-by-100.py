def a(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    return (a(n-1) * a(n-2)) % 100

N = int(input())

# Please write your code here.
print(a(N))