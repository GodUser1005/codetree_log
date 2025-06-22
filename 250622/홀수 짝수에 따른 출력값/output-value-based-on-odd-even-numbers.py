def summation_odd_even(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    return n + summation_odd_even(n-2)

N = int(input())

# Please write your code here.
print(summation_odd_even(N))