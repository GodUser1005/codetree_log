n = int(input())
s = 0
for _ in range(n):
    s += int(input())

print(s,float(f"{s/n:.1f}"))