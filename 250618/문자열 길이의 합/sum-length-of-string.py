n = int(input())
length = 0
cnt = 0
for _ in range(n):
    string = input()
    length += len(string)
    if string[0] == 'a':
        cnt += 1

print(length, cnt)