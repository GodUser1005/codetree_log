def is_in_3_6_9(n):
    string = str(n)
    for c in string:
        if c == '3' or c == '6' or c == '9':
            return True
    return False

def cnt_magic_num(a,b):
    cnt = 0
    for i in range(a,b+1):
        if i % 3 == 0 or is_in_3_6_9(i):
            cnt += 1
    return cnt


a, b = map(int, input().split())

# Please write your code here.
print(cnt_magic_num(a,b))