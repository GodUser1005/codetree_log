book = ["John", "Tom", "Paul"]
n = int(input())
if n in range(1,4):
    print(book[n-1])
else:
    print("Vacancy")