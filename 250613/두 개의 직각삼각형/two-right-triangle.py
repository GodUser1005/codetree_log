n = int(input())
for i in range(n):
    print('*'*(n-i),end="")
    print(' '*i*2,end="")
    print('*'*(n-i),end="")
    print()