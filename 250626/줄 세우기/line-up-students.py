n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.
students.sort(key=lambda student: (-student[0],-student[1],student[2]))

for s in students:
    print(s[0],s[1],s[2])