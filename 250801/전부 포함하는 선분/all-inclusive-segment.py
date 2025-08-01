n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

segments.sort(key = lambda x: (x[0],x[1]))

cand_1 = segments[-1][1] - segments[1][0]
cand_2 = segments[-2][1] - segments[0][0]

print(min(cand_1,cand_2))