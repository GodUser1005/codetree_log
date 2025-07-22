n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
def function():
    for i in range(11):
        for j in range(i+1,11):
            for k in range(j+1,11):
                satisfied = True
                for p in range(n):
                    if x[p] not in [i,j,k]:
                        satisfied = False
                        break
                if satisfied:
                    return True
    for i in range(11):
        for j in range(i+1,11):
            for k in range(j+1,11):
                satisfied = True
                for p in range(n):
                    if y[p] not in [i,j,k]:
                        satisfied = False
                        break
                if satisfied:
                    return True
    for i in range(11):
        for j in range(i+1,11):
            for k in range(11):
                satisfied = True
                for p in range(n):
                    if not (x[p] in [i,j] or y[p] == k):
                        satisfied = False
                        break
                if satisfied:
                    return True
    
    for i in range(11):
        for j in range(i+1,11):
            for k in range(11):
                satisfied = True
                for p in range(n):
                    if not (y[p] in [i,j] or x[p] == k):
                        satisfied = False
                        break
                if satisfied:
                    return True
    return False

print(int(function()))



    

                    