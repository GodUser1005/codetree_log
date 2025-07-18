n = int(input())
lines = [tuple(map(int,input().split())) for _ in range(n)]

MAX_POS = 100

count = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            satisfied = True
            arr = [0] * (MAX_POS + 1)
            for l in range(n):
                if l == i or l == j or l == k:
                    continue
                a,b = lines[l]
                for m in range(a,b+1):
                    arr[m] += 1
            for l in range(len(arr)):
                if arr[l] > 1:
                    satisfied = False
                    break
            if satisfied:
                count += 1
print(count)



