arr = list(map(int,input().split()))
arr = arr[:10]
arr = [a for a in arr if a != 0]
for i in arr[::-1]:
    print(i,end=" ")
