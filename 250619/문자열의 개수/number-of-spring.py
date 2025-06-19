arr = []
s = input()
while s != '0':
    arr.append(s)
    s = input()

print(len(arr))
for string in arr[::2]:
    print(string)
