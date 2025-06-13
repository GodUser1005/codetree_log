a = [int(input()) for _ in range(5)]
satisfied = True
for i in a:
    if i % 3 != 0:
        satisfied = False
        break
print(int(satisfied))