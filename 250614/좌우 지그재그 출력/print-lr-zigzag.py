n = int(input())
cnt = 1
diff = 1
for i in range(1,n**2+1):
    print(cnt,end=" ")
    if i % n == 0:
        cnt += n
        diff *= -1
        print()
    else:
        cnt += diff