s = input()
c = input()
cnt = 0
for a in s:
    if a == c:
        cnt += 1

print(s.count(c))