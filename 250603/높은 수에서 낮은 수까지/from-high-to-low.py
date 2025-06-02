a,b = map(int,input().split())
a,b = a if a > b else b, b if a > b else a
for i in range(a,b-1,-1):
    print(i,end=" ")