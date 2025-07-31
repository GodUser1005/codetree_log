board = [list(input()) for _ in range(10)]

# Please write your code here.
l_r, l_c, b_r,b_c = 0,0,0,0
for i in range(10):
    for j in range(10):
        if board[i][j] == 'L':
            l_r, l_c = i,j
        elif board[i][j] == 'B':
            b_r, b_c = i,j
if l_r == b_r or l_c == b_c:
    print(abs(l_r-b_r) + abs(l_c-b_c) + 2)
else:
    print(abs(l_r-b_r) + abs(l_c-b_c) - 1)
