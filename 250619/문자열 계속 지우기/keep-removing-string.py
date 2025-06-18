A = input()
B = input()

# Please write your code here.
while B in A:
    idx = A.find(B)
    arr = list(A)
    for _ in range(len(B)):
        arr.pop(idx)
    A = ''.join(arr)
print(A)