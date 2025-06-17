n,q = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        print(arr[query[1]-1])
    elif query[0] == 2:
        if query[1] not in arr:
            print(0)
        else:
            print(arr.index(query[1]) + 1)
    elif query[0] == 3:
        s,e = query[1],query[2]
        for a in arr[s-1:e]:
            print(a,end=" ")
        print()