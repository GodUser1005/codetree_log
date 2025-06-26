m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
week_of_days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
sum_days = [0]
for i in range(12):
    sum_days.append(sum_days[i] + days[i+1])

diff = (sum_days[m2-1]+d2)-(sum_days[m1-1]+d1)
result = diff // 7
for i in range(diff % 7 + 1):
    if week_of_days[i] == A:
        result += 1
        break

print(result)
