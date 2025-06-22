def cnt_function(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + cnt_function(n//2)
    else:
        return 1 + cnt_function(n//3)

N = int(input())

# Please write your code here.
print(cnt_function(N))
