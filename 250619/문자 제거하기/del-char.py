string = input()
while len(string) > 1:
    string = list(string)
    i = int(input())
    if i > len(string)-1:
        i = len(string)-1
    string.pop(i)
    string = ''.join(string)
    print(string)