n = int(input())
diff = n
arr = []
cnt = 0
while cnt < 2:
    if n % 5 == 0:
        cnt += 1
    arr.append(n)
    n += diff
for a in arr:
    print(a,end=" ")