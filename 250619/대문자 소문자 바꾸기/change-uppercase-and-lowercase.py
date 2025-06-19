string = input()

for c in string:
    if c.upper() == c:
        print(c.lower(),end="")
    elif c.lower() == c:
        print(c.upper(),end="")