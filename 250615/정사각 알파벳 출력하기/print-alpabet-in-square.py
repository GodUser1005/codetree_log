n = int(input())
ascii = ord('A')
for _ in range(n):
    for _ in range(n):
        print(chr(ascii),end="")
        ascii += 1
    print()
