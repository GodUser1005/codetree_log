def is_right_date(m,d):
    if not (1 <= m <= 12):
        return False
    dates = [31,28,31,30,31,30,31,31,30,31,30,31]
    if not (1 <= d <= dates[m-1]):
        return False
    return True

M, D = map(int, input().split())

# Please write your code here.
print("Yes" if is_right_date(M,D) else "No")