arr = [1]
n = int(input())

arr.append(n)

print(arr[0],arr[1],end=" ")
temp = 0
while temp < 100:
    temp = arr[0] + arr[1]
    print(temp,end=" ")
    arr[0] = arr[1]
    arr[1] = temp
