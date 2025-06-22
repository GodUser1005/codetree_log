def lcm(arr):
    prod = 1
    for e in arr:
        prod *= e
    if prod == 1:
        return 1
    for d in [2,3,5,7]:
        if prod % d == 0:
            for i in range(len(arr)):
                if arr[i] % d == 0:
                    arr[i] //= d
            return d * lcm(arr)

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
print(lcm(arr))
