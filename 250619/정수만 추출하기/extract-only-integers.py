a,b = input().split()

for i in range(len(a)):
    if not a[i].isdigit():
        a = int(a[:i])
        break
    

for i in range(len(b)):
    if not b[i].isdigit():
        b = int(b[:i])
        break

print(a+b)
