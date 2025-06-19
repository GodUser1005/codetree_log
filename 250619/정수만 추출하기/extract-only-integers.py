a,b = input().split()

if not a.isdigit():
    for i in range(len(a)):
        if not a[i].isdigit():
            a = int(a[:i])
            break
    
if not b.isdigit():
    for i in range(len(b)):
        if not b[i].isdigit():
            b = int(b[:i])
            break

print(a+b)
