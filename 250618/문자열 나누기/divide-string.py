n = int(input())
arr = list(input().split())
string = "".join(arr)
for i in range(0,len(string),5):
    if i+5 > len(string):
        print(string[i:])
    else:
        print(string[i:i+5])