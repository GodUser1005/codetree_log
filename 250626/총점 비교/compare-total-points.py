n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.

students = [(name[i],score1[i],score2[i],score3[i]) for i in range(n)]
students.sort(key=lambda s: s[1] + s[2] + s[3])

for student in students:
    for e in student:
        print(e,end=" ")
    print()