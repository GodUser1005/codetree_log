def is_palindrome(string):
    s = string[::-1]
    if s == string:
        return True
    return False

A = input()


# Please write your code here.

print("Yes" if is_palindrome(A) else "No")