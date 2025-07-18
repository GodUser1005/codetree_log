x,y = map(int,input().split())

def is_interesting_num(n):
    l = list(str(n))
    s = list(set(l))
    if len(s) == 2:
        a,b = 0,0
        for i in range(len(l)):
            if s[0] == l[i]:
                a += 1
            elif s[1] == l[i]:
                b += 1
        if a == 1 or b == 1:
            return True
    return False

count = 0
for i in range(x,y+1):
    if is_interesting_num(i):
        count += 1
print(count)
    