n = int(input())
arr = [2*i+2 for i in range(4)]
i = 0
for j in range(n**2):
    print(arr[i],end=" ")
    i += 1
    i %= 4
    if (j+1) % n == 0:
        print() 
