def push_back(arr, a):
    arr.append(a)

def pop_back(arr):
    arr.pop(-1)

def size(arr):
    print(len(arr))

def get(arr, k):
    print(arr[k-1])

n = int(input())

arr = []

for i in range(n):
    args = input().split()
    if len(args) >= 2:
        if args[0] == "push_back":
            push_back(arr, int(args[1]))
        elif args[0] == "get":
            get(arr, int(args[1]))
    else:
        if args[0] == "size":
            size(arr)
        elif args[0] == "pop_back":
            pop_back(arr)








            