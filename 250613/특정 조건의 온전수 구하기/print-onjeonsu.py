n = int(input())
for i in range(1,n+1):
    if not(i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0)):
        print(i,end=" ")