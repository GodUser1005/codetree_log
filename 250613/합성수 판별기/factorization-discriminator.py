n = int(input())
q = n

for i in range(2,n):
    if n % i == 0:
        q //= i
        break
print('C' if q < n else 'N')