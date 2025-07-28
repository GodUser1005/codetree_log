n,l = map(int,input().split())
arr = list(map(int,input().split()))
counts = [0] * 101
for i in arr:
    counts[i] += 1


def count_more_than_h(h):
    count = sum(counts[h:])
    return count

h = 1
while True:
    tmp = count_more_than_h(h)
    # print(tmp)
    if tmp >= h:
        h += 1
    elif l >= h - tmp:
        l -= (h - tmp)
        h += 1
    else:
        h -= 1
        break

print(h)
        
