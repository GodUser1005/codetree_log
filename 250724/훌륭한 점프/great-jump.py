n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = 0
for i in range(max(arr),max(arr[0],arr[-1])-1,-1):
    jump_cnt = k - 1
    for num in arr:
        jump_cnt -= 1
        if num <= i:
            jump_cnt = k
        elif jump_cnt <= 0:
            ans = i + 1
            break
    if ans > 0:
        break
ans = max(arr[-1],arr[0],ans)
    
print(ans)
