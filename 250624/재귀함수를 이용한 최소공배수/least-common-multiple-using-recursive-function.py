# def lcm(arr):
#     prod = 1
#     for e in arr:
#         prod *= e
#     if prod == 1:
#         return 1
#     for d in [2,3,5,7]:
#         if prod % d == 0:
#             for i in range(len(arr)):
#                 if arr[i] % d == 0:
#                     arr[i] //= d
#             return d * lcm(arr)

# n = int(input())
# arr = list(map(int, input().split()))

# # Please write your code here.
# print(lcm(arr))

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b,a % b)

def lcm(a,b):
    return a * b // gcd(a,b)


n = int(input())
arr = list(map(int,input().split()))

def get_lcm(index):
    if index == 0:
        return arr[0]
    return lcm(get_lcm(index-1),arr[index])

print(get_lcm(n-1))
