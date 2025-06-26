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
    for i in range(min(new_pos,pos),max(new_pos,pos)):
        arr[i] += 1
    pos = new_pos

count = 0
for c in arr:
    if c >= 2:
        count += 1

print(count)

