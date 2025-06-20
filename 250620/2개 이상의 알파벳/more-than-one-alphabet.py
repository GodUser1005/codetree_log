def is_more_2_alphabet(string):
    c = string[0]
    for i in string:
        if c != i:
            return True
    return False

A = input()

# Please write your code here.

print("Yes" if is_more_2_alphabet(A) else "No")