a = input()
queries = input()
for query in queries:
    if query == 'L':
        a = a[1:] + a[0]
    elif query == 'R':
        a = a[-1] + a[:-1]
    
print(a)