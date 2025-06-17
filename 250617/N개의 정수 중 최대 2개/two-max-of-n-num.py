n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_val = a[0]
first_idx = 0
for i in range(1,len(a)):
    if max_val < a[i]:
        max_val = a[i]
        first_idx = i

print(max_val,end=" ")

a = a[:first_idx] + a[first_idx+1:]
max_val = a[0]
for i in range(1,len(a)):
    if max_val < a[i]:
        max_val = a[i]

print(max_val,end=" ")