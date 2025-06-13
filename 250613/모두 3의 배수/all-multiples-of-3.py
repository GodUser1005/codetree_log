a = list(map(int,input().split()))
satisfied = True
for i in a:
    if i % 3 != 0:
        satisfied = False
        break
print(int(satisfied))