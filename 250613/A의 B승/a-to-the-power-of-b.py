prod = 1
a,b = map(int,input().split())
for _ in range(b):
    prod *= a
print(prod)