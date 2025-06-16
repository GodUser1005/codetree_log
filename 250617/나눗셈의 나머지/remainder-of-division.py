arr = []
a,b = map(int,input().split())
while a > 1:
    d = a % b
    a //= b
    arr.append(d)

count_arr = [0]*b
for i in arr:
    count_arr[i] += 1
print(sum([i**2 for i in count_arr]))
