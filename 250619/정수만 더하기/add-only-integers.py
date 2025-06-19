string = input()

s = 0

for c in string:
    if c.isdigit():
        s += int(c)

print(s)