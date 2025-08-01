n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
avg_blocks = sum(blocks) // n

count = 0
for block in blocks:
    if avg_blocks > block:
        count += avg_blocks - block

print(count)