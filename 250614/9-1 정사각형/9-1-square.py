arr = [i for i in range(9,0,-1)]
n = int(input())
index = 0
for i in range(n**2):
    print(arr[index],end="")
    index += 1
    index %= 9
    if (i+1) % n == 0:
        print()