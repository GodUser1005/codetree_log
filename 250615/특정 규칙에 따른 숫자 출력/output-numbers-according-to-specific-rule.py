n = int(input())
arr = [1,2,3,4,5,6,7,8,9]
index = 0
for i in range(n):
    print("  "*i,end="")
    for j in range(n-i):
        print(arr[index],end=" ")
        index += 1
        index %= 9
    print()
