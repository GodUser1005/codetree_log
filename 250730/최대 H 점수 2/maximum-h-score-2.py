n,l = map(int,input().split())
arr = list(map(int,input().split()))

def count_h(h):
    count = 0
    for num in arr:
        if num >= h:
            count += 1
    return count

cur_h = 1
for i in range(1,n+1):
    if count_h(i) >= i:
        cur_h = i
    else:
        break

while True:
    next_h = cur_h + 1
    count_cur = count_h(cur_h)
    count_next = count_cur - count_h(next_h)
    if l >= count_next and count_h(next_h) + count_next >= next_h:
        l -= (count_h(next_h) + count_next - next_h)
        cur_h += 1
    else:
        break

print(cur_h)

        
