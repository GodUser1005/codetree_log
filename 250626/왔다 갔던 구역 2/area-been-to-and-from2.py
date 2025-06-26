n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
arr = [0]*2001
pos = 1000
for i in range(n):
    xi = x[i]
    di = dir[i]
    new_pos = pos + (xi if di == 'R' else -xi)
    for j in range(min(pos,new_pos),max(pos,new_pos)):
        arr[j] += 1
    pos = new_pos

count = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        count += 1

print(count)