mat_1 = [list(map(int,input().split())) for _ in range(3)]
input()
mat_2 = [list(map(int,input().split())) for _ in range(3)]

result = [[mat_1[i][j] * mat_2[i][j] for j in range(3)] for i in range(3)]

for row in result:
    for element in row:
        print(element,end=" ")
    print()