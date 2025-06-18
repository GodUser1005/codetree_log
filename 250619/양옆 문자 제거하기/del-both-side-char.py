string = list(input())
string.pop(1)
string.pop(len(string)-2)
print(''.join(string))