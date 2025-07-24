n = int(input())
str = input()

# Please write your code here.
def is_double(sub_str):
    length = len(sub_str)
    count = 0
    for i in range(n-len(sub_str)+1):
        if str[i:i+len(sub_str)] == sub_str:
            count += 1
    return count >= 2

for l in range(1,n+1):
    checked = False
    for i in range(n-l+1):
        sub_str = str[i:i+l]
        if is_double(sub_str):
            checked = True
            break
    if not checked:
        print(l)
        break

