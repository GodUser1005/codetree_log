a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

ans = 0
if a <= c <= b or c <= a <= d:
    ans = max(d-a,b-c)
else:
    ans = b-a + d-c

print(ans)