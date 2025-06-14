n = int(input())
cnt = 1
for i in range(1,n+1):
    for _ in range(1,i+1):
        print(cnt,end=" ")
        cnt += 1
    print()