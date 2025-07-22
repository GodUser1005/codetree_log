inp = [input() for _ in range(3)]

# Please write your code here.

count = 0

def win(a,b):
    satisfied = True
    for r in range(3):
        if inp[r][0] == inp[r][1] == inp[r][2]:
            continue
        for c in range(3):
            if inp[r][c] not in [a,b]:
                satisfied = False
                break
        if satisfied:
            return True
    
    for c in range(3):
        if inp[0][c] == inp[1][c] == inp[2][c]:
            continue
        for r in range(3):
            if inp[r][c] not in [a,b]:
                satisfied = False
                break
        if satisfied:
            return True
    
    

for i in range(1,10):
    for j in range(i+1,10):
        a = 5
                    

        