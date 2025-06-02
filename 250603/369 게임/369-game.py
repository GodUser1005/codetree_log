n = int(input())
for i in range(1,n+1):
    print(0 if i % 3 == 0 or "3" in f"{i}" or "6" in f"{i}" or "9" in f"{i}" else i,end=" ")