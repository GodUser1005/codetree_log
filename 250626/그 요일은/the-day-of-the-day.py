m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
sum_days = [0]
for i in range(12):
    sum_days.append(sum_days[i] + days[i+1])

diff = (sum_days[m2-1]+d2)-(sum_days[m1-1]+d1)

print(diff // 7 + 1)
