n = int(input())
cnt = 1
diff = 1
for _ in range(n):
    for j in range(n):
        print(cnt,end="")
        cnt += diff
        if cnt < 1:
            cnt = 1
            diff *= -1
        elif cnt > n:
            cnt = n
            diff *= -1
    print()
