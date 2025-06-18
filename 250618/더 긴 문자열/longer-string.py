a,b = input().split()

len_a = len(a)
len_b = len(b)

if len_a > len_b:
    print(a,len_a)
elif len_a < len_b:
    print(b,len_b)
else:
    print('same')