x,y = map(int,input().split())

def is_interesting_num(n):
    l = list(str(n))
    l.sort()
    c = 0
    for i in range(len(l)-1):
        if l[i] != l[i+1]:
            c += 1
    if c != 1:
        return False
    return True

count = 0
for i in range(x,y+1):
    if is_interesting_num(i):
        count += 1
print(count)
    