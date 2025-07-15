board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
n = 19

def is_win(pos):
    ans = 0
    r,c = pos
    color = board[r][c]
    if color == 0:
        return ans
    if c + 4 < n:
        for i in range(5):
            if board[r][c+i] == color:
                ans = 1
            else:
                ans = 0
                break
    if (not ans) and r + 4 < n:
        for i in range(5):
            if board[r+i][c] == color:
                ans = 2
            else:
                ans = 0
                break
    if (not ans) and r + 4 < n and c - 4 >= 0:
        for i in range(5):
            if board[r+i][c-i] == color:
                ans = 3
            else:
                ans = 0
                break
    if (not ans) and r + 4 < n and c + 4 < n:
        for i in range(5):
            if board[r+i][c+i] == color:
                ans = 4
            else:
                ans = 0
                break
    return ans

ans = 0
ans_pos = [0,0]
for r in range(19):
    for c in range(19):
        win_num = is_win((r,c))
        if win_num > 0:
            ans = board[r][c]
            if win_num == 1:
                ans_pos = [r,c+2]
            elif win_num == 2:
                ans_pos = [r+2,c]
            elif win_num == 3:
                ans_pos = [r+2,c-2]
            elif win_num == 4:
                ans_pos = [r+2,c+2]


print(ans)
if ans > 0:
    print(ans_pos[0]+1,ans_pos[1]+1)
            