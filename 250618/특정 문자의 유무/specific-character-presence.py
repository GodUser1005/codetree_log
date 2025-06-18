string = input()
isIncluded = [False,False]
for i in range(len(string)-1):
    if string[i] == 'e' and string[i+1] == 'e':
        isIncluded[0] = True
    if string[i] == 'a' and string[i+1] == 'b':
        isIncluded[1] = True

for element in isIncluded:
    print('Yes' if element else 'No',end=" ")
