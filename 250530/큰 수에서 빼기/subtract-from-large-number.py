a,b = map(int,input().split())
result = 0
if a > b:
    result = a - b
else:
    result = b - a
print(result)