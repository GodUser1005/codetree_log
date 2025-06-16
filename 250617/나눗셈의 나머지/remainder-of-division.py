arr = []
a,b = map(int,input().split())
while a >= 1:
    d = a % b
    a //= b
    arr.append(d)

count_arr = [0]*b
for a in arr:
    count_arr[a] += 1
print(sum([i**2 for i in count_arr]))
