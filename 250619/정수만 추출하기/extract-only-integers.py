a,b = input().split()

int_a = ""
int_b = ""

for c in a:
    if c.isdigit():
        int_a += c
    else:
        break

for c in b:
    if c.isdigit():
        int_b += c
    else:
        break

print(int(int_a)+int(int_b))
