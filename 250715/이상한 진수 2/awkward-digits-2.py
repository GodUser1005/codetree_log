a = list(input())

# Please write your code here.
change = False
for i in range(1,len(a)):
    if a[i] == '0':
        a[i] = '1'
        change = True
        break
if not change:
    a[len(a)-1] = '0'

ans = 0
for i in range(len(a)):
    ans *= 2
    if a[i] == '1':
        ans += 1

print(ans)
