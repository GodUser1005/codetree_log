a = list(input())

# Please write your code here.
for i in range(1,len(a)):
    if a[i] == '0':
        a[i] = '1'
        break

ans = 0
for i in range(len(a)):
    ans *= 2
    if a[i] == '1':
        ans += 1

print(ans)
