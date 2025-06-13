a,b,c = map(int,input().split())
print("YES" if not(b//c-a//c) else "NO")