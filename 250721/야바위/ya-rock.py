n = int(input())
log = [tuple(map(int,input().split())) for _ in range(n)]

pos = [0,1,2]

score = 0
def cal_score(arr,a,b,c):
    a -= 1
    b -= 1
    c -= 1
    global score
    arr[a],arr[b] = arr[b],arr[a]
    if arr[c] == 1:
        score += 1

max_score = 0
for i in pos:
    tmp = [0]*3
    tmp[i] = 1
    for j in range(n):
        cal_score(tmp,log[i][0],log[i][1],log[i][2])
    max_score = max(score,max_score)
    score = 0

print(max_score)


