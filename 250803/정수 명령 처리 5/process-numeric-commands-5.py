n = int(input())
commands = []
for _ in range(n):
    commands.append(list(input().split()))

arr = []
for command in commands:
    if len(command) == 2:
        c,num = command
        num = int(num)
        if c == 'push_back':
            arr.append(num)
        else:
            print(arr[num-1])
    else:
        c, = command
        if c == 'pop_back':
            arr.pop()
        else:
            print(len(arr))



            