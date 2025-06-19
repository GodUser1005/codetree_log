def gcd(n,m):
    if n < m:
        n,m = m,n
    if m == 0:
        return n
    return gcd(m,n%m)

n, m = map(int, input().split())

# Please write your code here.
print(gcd(n,m))