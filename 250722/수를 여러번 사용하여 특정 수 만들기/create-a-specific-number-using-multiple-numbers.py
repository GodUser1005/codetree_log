A, B, C = map(int, input().split())

# Please write your code here.
max_ans = 0

for i in range(C//A + 1):
    for j in range(1,i+1):
        a_count = i - j
        b_count = j
        ans = A * a_count + B * b_count
        if ans <= C:
            max_ans = max(max_ans,ans)
        else:
            break

print(max_ans)


    


