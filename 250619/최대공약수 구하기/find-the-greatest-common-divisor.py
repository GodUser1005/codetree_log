def euclid_gcd(n,m):
    if n < m:
        n,m = m,n
    if m == 0:
        return n
    return gcd(m,n%m)

def gcd(n,m):
    gcd = 1
    for i in range(1,min(n,m)+1):
        if n % i == 0 and m % i == 0:
            gcd = i
    return gcd

n, m = map(int, input().split())

# Please write your code here.
# print(euclid_gcd(n,m))
print(gcd(n,m))