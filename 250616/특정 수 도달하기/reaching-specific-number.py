arr = list(map(int,input().split()))
s = 0
cnt = 0
for i in arr:
    if i >= 250:
        break
    s += i
    cnt += 1
print(s,f"{s/cnt:.1f}")
    