scores = list(map(int,input().split()))
count = [0]*11
for score in scores:
    if score == 0:
        break
    count[score//10] += 1

for i in range(len(count)-1,0,-1):
    print(f"{i*10} - {count[i]}")