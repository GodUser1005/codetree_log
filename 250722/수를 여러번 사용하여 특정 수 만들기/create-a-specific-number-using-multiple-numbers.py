A, B, C = map(int, input().split())

# Please write your code here.
diff = B - A
max_count = C // A
ans = A * max_count
for i in range(max_count):
    ans += diff
    if ans > C:
        ans -= diff
        break
print(ans)
    


