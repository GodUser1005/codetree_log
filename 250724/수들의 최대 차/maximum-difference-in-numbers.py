n,k = map(int,input().split())
seq = [int(input()) for _ in range(n)]

min_seq = min(seq)
max_seq = max(seq)

max_cnt = 0
for i in range(min_seq, max(max_seq + 1 - k, min_seq+k -1)):
    cnt = 0
    for num in seq:
        if i <= num <= i + k:
            cnt += 1
    max_cnt = max(cnt,max_cnt)
print(max_cnt)
