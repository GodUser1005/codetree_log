strings = ['apple','banana','grape','blueberry','orange']

cnt = 0
c = input()
for string in strings:
    if c in string[2:4]:
        print(string)
        cnt += 1

print(cnt)