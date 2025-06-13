cnt = 0
s = 0
while True:
    n = int(input())
    if 20 <= n < 30:
        s += n
        cnt += 1
    else:
        break
print(f"{s/cnt:.2f}")