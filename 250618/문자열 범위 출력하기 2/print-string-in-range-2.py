string = input()
n = int(input())
if n > len(string):
    n = len(string)
for i in range(-1,-1*n - 1, -1):
    print(string[i],end="")