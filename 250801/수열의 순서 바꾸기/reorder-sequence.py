n = int(input())
sequence = [0] + list(map(int, input().split()))

# Please write your code here.

last_index = 0
for i in range(1,n):
    if sequence[i] > sequence[i+1]:
        last_index = i

print(last_index)
