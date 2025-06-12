a = int(input())
for i in range(1,a+1):
    if not((i % 2 == 0 and i % 4 != 0) or (i // 8) % 2 == 0 or i % 7 < 4):
        print(i,end=" ")