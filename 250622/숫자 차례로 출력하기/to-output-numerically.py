def preorder(n):
    if n == 0:
        return
    print(n,end=" ")
    preorder(n-1)

def postorder(n):
    if n == 0:
        return
    postorder(n-1)
    print(n,end=" ")

n = int(input())

# Please write your code here.
postorder(n)
print()
preorder(n)