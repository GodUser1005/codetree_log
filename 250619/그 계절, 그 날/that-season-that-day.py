def is_leap_year(y):
    if y % 4 != 0:
        return False
    if y % 100 == 0 and y % 400 != 0:
        return False
    return True

def date_list(y):
    dates = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(y):
        dates[1] = 29
    return dates

def is_right_date(y,m,d):
    dates = date_list(y)
    if 1 <= d <= dates[m-1]:
        return True
    return False

Y, M, D = map(int, input().split())

# Please write your code here.
if is_right_date(Y,M,D):
    if 3 <= M <= 5:
        print("Spring")
    elif 6 <= M <= 8:
        print("Summer")
    elif 9 <= M <= 11:
        print("Fall")
    elif M == 12 or 1 <= M <= 2:
        print("Winter")
else:
    print(-1)