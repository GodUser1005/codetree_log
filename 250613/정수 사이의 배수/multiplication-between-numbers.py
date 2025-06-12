a,b = map(int,input().split())
cnt = 0
s = 0
for i in range(a,b+1):
    if i % 5 == 0 or i % 7 == 0:
        s += i
        cnt += 1

print(s,f"{s/cnt:.1f}")