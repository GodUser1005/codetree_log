import sys
MAX_INT = sys.maxsize

arr = list(map(int, input().split()))

# Please write your code here.
ans = MAX_INT
for i in range(5):
    for j in range(5):
        if i == j:
            continue
        for k in range(5):
            if i == k or j == k:
               continue
            t = []
            t.append(arr[i])
            t.append(arr[j] + arr[k])
            t.append(sum(arr) - t[0] - t[1])
            if t[0] == t[1] or t[0] == t[2] or t[1] == t[2]:
                continue
            ans = min(ans,max(t)-min(t))
    
if ans == MAX_INT:
    ans = -1
print(ans)
            