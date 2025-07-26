n, k = map(int, input().split())
num = [int(input()) for _ in range(n)]

# Please write your code here.
def index_in_range(i):
    return 0 <= i <= n-1

bombs = []
for i in range(n):
    for j in range(i-k,i+k+1):
        if index_in_range(j):
            if num[i] == num[j] and i != j:
                bombs.append(num[i])
                break

bombs.sort()

max_count = 0
prev_num = -1
count = 0
ans = -1
for i in range(len(bombs)):
    if prev_num == bombs[i]:
        count += 1
        if max_count <= count:
            ans = bombs[i]
            max_count = count
    else:
        count = 1
        prev_num = bombs[i]

print(ans)


