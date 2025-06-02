a,b = map(int,input().split())
while a <= b:
    print(a,end=" ")
    a = 2*a if a % 2 == 1 else 3+a