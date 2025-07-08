N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

count_arr = [0] * (N+1)

answer = -1
for s in student:
    count_arr[s] += 1
    if count_arr[s] >= K:
        answer = s 
        break

print(answer)