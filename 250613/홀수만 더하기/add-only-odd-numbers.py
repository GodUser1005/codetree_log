n = int(input())
result = 0
for _ in range(n):
    a = int(input())
    if a % 2 == 1 and a % 3 == 0:
        result += a

print(result)