cnt = 0
for _ in range(3):
    a,t = input().split()
    if a == "Y":
        if int(t) >= 37:
            cnt += 1

if cnt >= 2:
    print("E")
else:
    print("N")