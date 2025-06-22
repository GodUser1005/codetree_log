n = int(input())

# Please write your code here.

def print_n(n):
    if n == 0:
        return
    print("HelloWorld")
    print_n(n-1)

print_n(n)
