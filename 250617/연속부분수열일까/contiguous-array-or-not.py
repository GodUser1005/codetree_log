n1,n2 = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
satisfied = False
for i in range(n1-n2 + 1):
    if a[i] == b[0]:
        for j in range(n2):
            if a[i+j] == b[j]:
                satisfied = True
            else:
                satisfied = False
                break
        if satisfied:
            break
print('Yes' if satisfied else 'No')
    
