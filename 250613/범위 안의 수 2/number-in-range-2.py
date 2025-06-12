s = 0
cnt = 0
for _ in range(10):
    n = int(input())
    if 0 <= n <= 200:
        s += n
        cnt += 1
print(s,f"{s/cnt:.1f}")