n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

def is_equal(a,b):
    for i in range(len(a)):
        if a[i] !=  b[i]:
            return False
    return True

print("Yes" if is_equal(A,B) else "No")
