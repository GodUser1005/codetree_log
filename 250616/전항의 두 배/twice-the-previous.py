arr = list(map(int,input().split()))
for _ in range(8):
    arr.append(arr[-1] + 2*arr[-2])

for a in arr:
    print(a,end=" ")