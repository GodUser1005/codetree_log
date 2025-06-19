string = input()

for c in string:
    if c.isalpha():
        print(c.upper(),end="")