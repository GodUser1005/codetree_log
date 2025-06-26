n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0]*101
for segment in segments:
    for i in range(segment[0],segment[1]+1):
        arr[i] += 1

print(max(arr))