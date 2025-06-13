while True:
    w,h,c = input().split()
    w,h = map(int,[w,h])
    print(w*h)
    if c == 'C':
        break

