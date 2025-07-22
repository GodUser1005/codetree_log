inp = [list(map(int,list(input()))) for _ in range(3)]

# Please write your code here.

def row_win(a,b):
    for r in range(3):
        satisfied = True
        if inp[r][0] == inp[r][1] and inp[r][0] == inp[r][2]:
            continue
        for c in range(3):
            if inp[r][c] not in [a,b]:
                satisfied = False
                break
        if satisfied:
            return True
    return False

def col_win(a,b):
    for c in range(3):
        satisfied = True
        if inp[0][c] == inp[1][c] == inp[2][c]:
            continue
        for r in range(3):
            if inp[r][c] not in [a,b]:
                satisfied = False
                break
        if satisfied:
            return True
    return False

def cross_win(a,b):
    l = list(set([inp[0][0],inp[1][1],inp[2][2]]))
    l.sort()
    if l == [a,b]:
        return True
    l = list(set([inp[2][0],inp[1][1],inp[0][2]]))
    l.sort()
    if l == [a,b]:
        return True
    return False
    

def win(a,b):
    if row_win(a,b):
        return True
    elif col_win(a,b):
        return True
    elif cross_win(a,b):
        return True
    return False
    
    
    
    
count = 0
for i in range(1,10):
    for j in range(i+1,10):
        if win(i,j):
            count += 1

print(count)
                    

        