cnt_3, cnt_5 = 0,0
for _ in range(10):
    a = int(input())
    if a % 3 == 0:
        cnt_3 += 1
    if a % 5 == 0:
        cnt_5 += 1
print(cnt_3, cnt_5)