s = input()

for c in s:
    if c.isalpha():
        print(c.lower(),end="")
    elif c.isdigit():
        print(c,end="")