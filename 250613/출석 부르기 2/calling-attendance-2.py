a = ['John','Tom','Paul','Sam']
while True:
    n = int(input())
    if 1 <= n <= 4:
        print(a[n-1])
    else:
        break
print('Vacancy')