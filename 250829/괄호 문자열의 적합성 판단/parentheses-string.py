s = input()
stack = []
ans = "Yes"

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if len(stack) == 0:
            ans = "No"
            break
        else:
            stack.pop()

if len(stack) != 0:
    ans = "No"

print(ans)


