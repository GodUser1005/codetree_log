mat = [list(map(int,input().split())) for _ in range(4)]
s = 0
for i in range(4):
    s += sum(mat[i][:i+1])
print(s)