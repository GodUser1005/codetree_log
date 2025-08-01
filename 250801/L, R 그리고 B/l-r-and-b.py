board = [list(input()) for _ in range(10)]

# Please write your code here.
l_r, l_c, b_r,b_c,r_r,r_c = 0,0,0,0,0,0
for i in range(10):
    for j in range(10):
        if board[i][j] == 'L':
            l_r, l_c = i,j
        elif board[i][j] == 'B':
            b_r, b_c = i,j
        elif board[i][j] == 'R':
            r_r, r_c = i,j

if l_c == b_c == r_c and min(l_r,b_r) < r_r < max(l_r,b_r):
    print(abs(l_r - b_r) + 1)
elif l_r == b_r == r_r and min(l_c,b_c) < r_c < max(l_c,b_c):
    print(abs(l_c - b_c) + 1)
else:
    print(abs(l_c - b_c) + abs(l_r - b_r) - 1)
