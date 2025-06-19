s = input()

for c in s:
    if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
        print(c.lower(),end="")
    elif '0' <= c <= '9':
        print(c,end="")