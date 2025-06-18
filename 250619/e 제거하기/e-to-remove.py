string = input()
arr = list(string)
arr.pop(string.find('e'))
print(''.join(arr))
