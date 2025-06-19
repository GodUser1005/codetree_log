n = int(input())
s = 0
for _ in range(n):
    s += int(input())

s = str(s)
s = s[1:] + s[0]
print(s)