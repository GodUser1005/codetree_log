n = int(input())
log = [tuple(map(int,input().split())) for _ in range(n)]

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
for i in range(3):
    tmp = [0]*3
    tmp[i] = 1
    for j in range(n):
        cal_score(tmp,log[j][0],log[j][1],log[j][2])
    max_score = max(score,max_score)
    score = 0

print(max_score)


