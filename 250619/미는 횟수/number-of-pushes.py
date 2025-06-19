a = input()
b = input()

n = -1
for i in range(1,len(b)):
    a = a[-1] + a[:-1]
    if a == b:
        n = i

print(n)
        