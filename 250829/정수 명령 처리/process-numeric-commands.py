def stack(arr):
    c = list(input().split())
    if len(c) == 2:
        arr.append(int(c[1]))
    else:
        if c[0] == "pop":
            print(arr[-1])
            arr.pop()
        elif c[0] == "size":
            print(len(arr))
        elif c[0] == "empty":
            print(int(len(arr) == 0))
        elif c[0] == "top":
            print(arr[-1])

arr = []
n = int(input())
for _ in range(n):
    stack(arr)

