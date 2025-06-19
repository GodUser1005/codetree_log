def is_contiguous_subsequence(a,b):
    for i in range(len(a)-len(b)+1):
        satisfied = True
        for j in range(len(b)):
            if a[i+j] != b[j]:
                satisfied = False
                break
        if satisfied:
            return satisfied
    return False

n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
print("Yes" if is_contiguous_subsequence(a,b) else "No")