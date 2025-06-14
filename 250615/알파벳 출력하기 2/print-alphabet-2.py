n = int(input())
ascii = ord('A')
for i in range(n):
    print("  "*i,end="")
    for _ in range(n-i):
        print(chr(ascii),end=" ")
        ascii += 1
        if ascii > ord('Z'):
            ascii = ord('A')
    print()