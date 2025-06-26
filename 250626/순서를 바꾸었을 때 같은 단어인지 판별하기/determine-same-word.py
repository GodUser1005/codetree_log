word1 = input()
word2 = input()

# Please write your code here.
def is_equal(a,b):
    if len(a) == len(b):
        a_list = list(a)
        b_list = list(b)
        a_list.sort()
        b_list.sort()

        if ''.join(a_list) == ''.join(b_list):
            return True
    return False

print("Yes" if is_equal(word1,word2) else "No")