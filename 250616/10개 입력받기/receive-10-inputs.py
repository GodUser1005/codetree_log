arr = list(map(int,input().split()))
temp = []
for a in arr:
    if a == 0:
        break
    temp.append(a)
print(sum(temp),f"{sum(temp)/len(temp):.1f}")