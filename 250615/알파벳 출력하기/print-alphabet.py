n = int(input())
ascii = ord('A')
for i in range(1,n+1):
    for _ in range(i):
        print(chr(ascii),end="")
        ascii += 1
        if ascii == ord('Z') + 1:
            ascii = ord('A')
    print()
