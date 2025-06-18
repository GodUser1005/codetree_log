A = input()

# Please write your code here.
prev = A[0]
cnt = 0
result = prev
for char in A:
    if prev == char:
        cnt += 1
    else:
        result += str(cnt)
        cnt = 1
        prev = char
        result += char
if cnt > 1:
    result += str(cnt)

print(len(result))
print(result)
