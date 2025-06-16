n = int(input())
arr = list(map(int,input().split()))
for i in [a for a in arr if a % 2 == 0]:
    print(i,end=" ")