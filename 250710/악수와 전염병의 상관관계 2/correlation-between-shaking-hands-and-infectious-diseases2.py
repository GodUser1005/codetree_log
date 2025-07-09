N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.

developers = [-1] * (N+1)
developers[P] = K
handshakes.sort(key=lambda x: x[0])

def handshake(x,y):
    if developers[x] < 0 and developers[y] < 0:
        return
    elif developers[x] > 0:
        developers[x] -= 1
        if developers[y] < 0:
            developers[y] = K
        elif developers[y] > 0:
            developers[y] -= 1
    elif developers[y] > 0:
        developers[y] -= 1
        if developers[x] < 0:
            developers[x] = K
    return

for h in handshakes:
    handshake(h[1],h[2])

for d in developers[1:]:
    print(0 if d < 0 else 1,end="")
