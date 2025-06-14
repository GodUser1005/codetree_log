n = int(input())
print("* "*n)
for i in range(1,n):
    for j in range(1,n+1):
        if j <= i or j == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    

