a,b,c = map(int,input().split())
a,b = a//c,b//c
print("YES" if b-a else "NO")