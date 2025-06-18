string, n = input().split()
n = int(n)
string = list(string)

for _ in range(n):
    t,a,b = input().split()
    t = int(t)
    if t == 1:
        a,b = int(a),int(b)
        string[a-1],string[b-1] = string[b-1], string[a-1]
    elif t == 2:
        for i in range(len(string)):
            if string[i] == a:
                string[i] = b
    print(''.join(string))


