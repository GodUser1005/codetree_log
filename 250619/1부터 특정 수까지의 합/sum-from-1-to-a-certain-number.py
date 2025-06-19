def sum_1_to_n(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s // 10

n = int(input())

# Please write your code here.
print(sum_1_to_n(n))