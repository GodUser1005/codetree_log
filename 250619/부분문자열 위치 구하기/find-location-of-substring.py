input_str = input()
target_str = input()

satisfied = True
result = -1

# Please write your code here.
for i in range(len(input_str) - len(target_str) + 1):
    for j in range(len(target_str)):
        if input_str[i+j] != target_str[j]:
            satisfied = False
            break
    if satisfied:
        result = i
        break
    satisfied = True

print(result)
        
