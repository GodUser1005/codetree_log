a = input()

cnt = 0
for i,c in enumerate(a):
    if c == '(':
        for c2 in a[i+1:]:
            if c2 == ')':
                cnt += 1

print(cnt)