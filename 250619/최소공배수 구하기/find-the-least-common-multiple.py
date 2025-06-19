def euclid_gcd(n,m):
    if n < m:
        n,m = m,n
    if m == 0:
        return n
    return euclid_gcd(m,n%m)

def lcm(n,m):
    gcd = euclid_gcd(n,m)
    return (m*n)//gcd

n, m = map(int, input().split())

# Please write your code here.
print(lcm(n,m))