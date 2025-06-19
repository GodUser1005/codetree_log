def print_sqaure(n):
    cnt = [1,2,3,4,5,6,7,8,9]
    idx = 0
    for _ in range(n):
        for _ in range(n):
            print(cnt[idx],end=" ")
            idx = (idx + 1) % 9
        print()

n = int(input())

# Please write your code here.
print_sqaure(n)