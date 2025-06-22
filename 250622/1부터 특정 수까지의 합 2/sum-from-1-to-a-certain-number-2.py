def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n-1)

N = int(input())

# Please write your code here.
print(recursive_sum(N))