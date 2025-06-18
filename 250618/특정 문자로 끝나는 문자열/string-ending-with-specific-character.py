arr = [input() for _ in range(10)]
c = input()
isExist = False
for element in arr:
    if element[-1] == c:
        print(element)
        isExist = True
if not isExist:
    print('None')