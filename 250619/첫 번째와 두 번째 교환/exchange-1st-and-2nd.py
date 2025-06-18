string = list(input())
c1,c2 = string[0],string[1]

for i in range(len(string)):
    if string[i] == c1:
        string[i] = c2
    elif string[i] == c2:
        string[i] = c1

print(''.join(string))