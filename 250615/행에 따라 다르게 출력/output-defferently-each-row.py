n = int(input())
cnt = 0
diff = 1
for i in range(1,n**2+1):
    cnt += diff
    print(cnt,end=" ")
    if i % n == 0:
        if (i // n) % 2 == 1:
            diff = 2
        else:
            diff = 1
        print()