string = list(input())
c2 = string[1]
for i in range(len(string)):
    if string[i] == c2:
        string[i] = string[0]
print(''.join(string))
