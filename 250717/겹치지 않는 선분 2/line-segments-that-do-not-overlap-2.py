n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
fold = [0] * n

for i in range(n):
    for j in range(i+1,n):
        if (lines[i][0]-lines[j][0]) * (lines[i][1] - lines[j][1]) < 0:
            fold[i] = 1
            fold[j] = 1

print(n-sum(fold))
