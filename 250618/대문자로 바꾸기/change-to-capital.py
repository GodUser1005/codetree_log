mat = [list(input().split()) for _ in range(5)]
for row in mat:
    for element in row:
        print(element.upper(),end=" ")
    print()