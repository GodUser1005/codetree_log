n = int(input())
arr = [2,4,6,8]
i = 0
for j in range(n**2):
    print(arr[i],end=" ")
    i += 1
    i %= 4
    if (j+1) % n == 0:
        print() 
