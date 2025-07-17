MAX_INT = 100

n = int(input())
arr = [0] * (MAX_INT + 1)

min_index = MAX_INT
max_index = 0
for _ in range(n):
    p,c = input().split()
    p = int(p)
    arr[p] = c
    min_index = min(min_index,p)
    max_index = max(max_index,p)

max_size = 0
for i in range(min_index,max_index+1):
    for j in range(i,max_index+1):
        if arr[i] != 0 and arr[j] != 0:
            count = {'G':0,'H':0}
            for k in range(i,j+1):
                if arr[k] == 'G':
                    count['G'] += 1
                elif arr[k] == 'H':
                    count['H'] += 1
            if count['G'] == 0 or count['H'] == 0 or count['G'] == count['H']:
                max_size = max(max_size,j-i)


print(max_size)
        
