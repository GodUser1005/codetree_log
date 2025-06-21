n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def print_value():
    global m
    s = 0
    while m >= 1:
        s += A[m-1]
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2
    print(s)


print_value()