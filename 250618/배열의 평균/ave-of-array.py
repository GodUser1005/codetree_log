mat = [list(map(int,input().split())) for _ in range(2)]

row_averages = [0,0]
for i in range(2):
    row_averages[i] = sum(mat[i])/len(mat[i])
    print(f"{row_averages[i]:.1f}",end=" ")
print()


column_averages = [0,0,0,0]
for i in range(4):
    column_sum = 0
    for j in range(2):
        column_sum += mat[j][i]
    column_averages[i] = column_sum/2
    print(f"{column_averages[i]:.1f}",end=" ")
print()

total_average = sum(row_averages)/2
print(f"{total_average:.1f}")
