n,m = map(int,input().split())
mat = [input() for _ in range(n)]

def count_lee(pos):
    count = 0
    r,c = pos
    if c + 2 < m and mat[r][c:c+3] == 'LEE':
        count += 1
    if c + 2 < m and mat[r][c:c+3] == 'EEL':
        count += 1
    if r + 2 < n:
        lee = 'LEE'
        is_lee = True
        is_eel = True
        for i in range(3):
            if mat[r+i][c] != lee[i]:
                is_lee = False
                break
        if is_lee:
            count += 1
        for i in range(3):
            if mat[r+i][c] != lee[-(i+1)]:
                is_eel = False
                break
        if is_eel:
            count += 1
    if r + 2 < n and c + 2 < m:
        lee = 'LEE'
        is_lee = True
        is_eel = True
        for i in range(3):
            if mat[r+i][c+i] != lee[i]:
                is_lee = False
                break
        if is_lee:
            count += 1
        for i in range(3):
            if mat[r+i][c+i] != lee[-(i+1)]:
                is_eel = False
                break
        if is_eel:
            count += 1
    if r + 2 < n and c - 2 >= 0:
        lee = 'LEE'
        is_lee = True
        is_eel = True
        for i in range(3):
            if mat[r+i][c-i] != lee[i]:
                is_lee = False
                break
        if is_lee:
            count += 1
        for i in range(3):
            if mat[r+i][c-i] != lee[-(i+1)]:
                is_eel = False
                break
        if is_eel:
            count += 1
    return count

count = 0
for r in range(n):
    for c in range(m):
        count += count_lee((r,c))

print(count)
    
        